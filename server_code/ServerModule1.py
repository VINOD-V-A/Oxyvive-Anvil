import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
import base64

@anvil.server.callable
def data(id,name,data):
  app_tables.datas.add_row(id=id, name=name, data=data)
  
@anvil.server.callable
def user(id,username,email,password,phone,pincode):
  app_tables.users.add_row(id=id, username=username, email=email, password=password,phone=phone,pincode=pincode)
  
@anvil.server.callable
def BookSlot(slot_id, user_id, username,book_date,book_time):
  app_tables.bookslot.add_row(slot_id=slot_id, user_id=user_id, username=username, book_date=book_date, book_time=book_time)

@anvil.server.callable
def create_media_object(content_type, file_data_base64, file_name):
    # Decode the base64 string to get the bytes data
    file_data = base64.b64decode(file_data_base64)
    media_object = anvil.media.BlobMedia(content_type, file_data, file_name)
    return media_object


@anvil.server.callable
def upload_file(path, data):
    # Encode the binary data to Base64 string
    data_base64 = base64.b64encode(data).decode('utf-8')
    
    # Add a new row to the datas table with the encoded data
    app_tables.datas.add_row(id=1, name=path, data=data_base64)