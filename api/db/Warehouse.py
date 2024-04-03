import logging
from ZODB import DB
from ZEO import ClientStorage
import transaction
import uuid
from fastapi import HTTPException

class Warehouse:
    def __init__(self, zeo_address):
        self.zeo_address = zeo_address
        self.db = None
        self.connection = None
        self.root = None
        self.logger = logging.getLogger(__name__)

    def connect(self):
        try:
            storage = ClientStorage.ClientStorage(self.zeo_address)
            self.db = DB(storage)
            self.connection = self.db.open()
            self.root = self.connection.root()
        except Exception as e:
            error_msg = f"Error connecting to ZODB: {str(e)}"
            self.logger.error(error_msg)
            raise HTTPException(status_code=500, detail=error_msg)

    def close(self):
        try:
            if self.connection is not None:
                self.connection.close()
                self.db.close()
        except Exception as e:
            error_msg = f"Error closing ZODB connection: {str(e)}"
            self.logger.error(error_msg)
            raise HTTPException(status_code=500, detail=error_msg)

    def create(self, obj):
        try:
            obj_id = str(uuid.uuid4())
            obj._id = obj_id  # Set the _id attribute of the object directly
            self.root[obj_id] = obj
            transaction.commit()
            return obj
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.logger.error(error_msg)
            transaction.abort()
            raise HTTPException(status_code=500, detail=error_msg)

    def findOne(self, obj_id):
        try:
            return self.root[obj_id]
        except KeyError:
            error_msg = f"Object not found with id: {obj_id}"
            self.logger.error(error_msg)
            raise HTTPException(status_code=404, detail=error_msg)
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.logger.error(error_msg)
            raise HTTPException(status_code=500, detail=error_msg)

    def findAll(self):
        try:
            return list(self.root.values())
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.logger.error(error_msg)
            raise HTTPException(status_code=500, detail=error_msg)

    def findOneAndUpdate(self, obj_id, new_obj):
        try:
            #replace the object with the new object
            new_obj._id = obj_id
            self.root[obj_id] = new_obj
            transaction.commit()
            return new_obj
        except KeyError:
            error_msg = f"Object not found with id: {obj_id}"
            self.logger.error(error_msg)
            raise HTTPException(status_code=404, detail=error_msg)

    def findOneAndDelete(self, obj_id):
        try:
            if obj_id in self.root:
                del_obj = self.root[obj_id]
                del self.root[obj_id]
                transaction.commit()
                return ("Deleted object successfully", del_obj)
            else:
                error_msg = f"Object not found with id: {obj_id}"
                self.logger.error(error_msg)
                raise KeyError("Object not found")
        except KeyError as e:
            self.logger.error(error_msg)
            transaction.abort()
            raise HTTPException(status_code=404, detail=error_msg)
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.logger.error(error_msg)
            transaction.abort()
            raise HTTPException(status_code=500, detail=error_msg)
