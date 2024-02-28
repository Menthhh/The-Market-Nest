from ZODB import DB
from ZODB.FileStorage import FileStorage
from fastapi import HTTPException
import transaction
import uuid

class Warehouse:
    def __init__(self, path):
        self.path = path
        self.db = None
        self.connection = None
        self.root = None

    def connect(self):
        storage = FileStorage(self.path)
        self.db = DB(storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()

    def create(self, obj):
        try:
            obj_id = str(uuid.uuid4())
            obj._id = obj_id
            self.root[obj_id] = obj
            transaction.commit()
            return obj
        except KeyError as e:
            transaction.abort()
            raise HTTPException(status_code=400, detail="KeyError occurred during object creation")
        except Exception as e:
            transaction.abort()
            raise HTTPException(status_code=500, detail=str(e))


    def findOne(self, obj_id):
        try:
            obj = self.root[obj_id]
            return obj
        except KeyError:
            return {"error": "Object not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500

    def findAll(self):
        try:
            root = []
            for key in self.root.keys():
                root.append(self.root[key])
            return root
        except Exception as e:
            return {"error": str(e)}, 500

    def findOneAndUpdate(self, obj_id, new_obj):
        try:
            if obj_id not in self.root:
                raise KeyError("Object not found")
            
            existing_obj = self.root[obj_id]

            # Update based on object instance
            if hasattr(new_obj, '__dict__'):
                for attr_name, attr_value in new_obj.__dict__.items():
                    if hasattr(existing_obj, attr_name):
                        setattr(existing_obj, attr_name, attr_value)
                    else:
                        raise ValueError(f"Attribute '{attr_name}' does not exist in the object")

            # Update based on dictionary
            elif isinstance(new_obj, dict):
                for attr_name, attr_value in new_obj.items():
                    if hasattr(existing_obj, attr_name):
                        setattr(existing_obj, attr_name, attr_value)
                    else:
                        raise ValueError(f"Attribute '{attr_name}' does not exist in the object")
            else:
                raise ValueError("Unsupported type for new_obj")

            transaction.commit()  # Commit changes
            return existing_obj
        except KeyError as e:
            transaction.abort()  # Abort transaction if object not found
            raise e
        except ValueError as e:
            transaction.abort()  # Abort transaction if attribute does not exist
            raise e
        except Exception as e:
            transaction.abort()  # Abort transaction in case of any error
            raise e



    def findOneAndDelete(self, obj_id):
        try:
            deleted_obj = self.root[obj_id]
            del self.root[obj_id]
            transaction.commit()
            return {"message": "Object deleted successfully", "obj":deleted_obj}, 200
        except KeyError:
            return {"error": "Object not found"}, 404
        except Exception as e:
            transaction.abort()
            return {"error": str(e)}, 500

    def deleteAll(self):
        try:
            print("Are you sure you want to delete all records? y/n")
            response = input()
            if response == "y":
                keys_to_delete = list(self.root.keys())
                for key in keys_to_delete:
                    del self.root[key]
                transaction.commit()
                return {"message": "All records have been deleted"}, 200
            else:
                return {"message": "Operation cancelled"}, 200
        except Exception as e:
            transaction.abort()
            return {"error": str(e)}, 500

