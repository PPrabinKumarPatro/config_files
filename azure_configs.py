import azure.storage.file.fileservice

fs = azure.storage.file.fileservice.FileService(
    account_name='sensitivedata', 
   sas_token='?sv=2019-07-29&ss=f&srt=co&sp=rdl&se=2021-01-01T03:08:51Z&st=2018-04-18T18:08:51Z&spr=https&sig=vcFB1aGXYJPEDekInetHOb9TsMGBheJ6%2Bjb6R8SIemk%3D')

fs.get_file_to_path('secrets', None, 'config.txt', 'config')
