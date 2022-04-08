# Insert values in a table
from google.cloud import bigqueryclient = bigquery.Client()
dataset_id = ‘test’# For this sample, the table must already exist and have a defined schematable_id = ‘test_table_creation’
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)# Creating a list of tuples with the values that shall be inserted into the tablerows_to_insert = [
(u’A’, 1),
(u’B’, 2),
]errors = client.insert_rows(table, rows_to_insert) 
print(errors)


from google.cloud import bigqueryclient = bigquery.Client()
dataset_id = ‘test’ # For this sample, the table must already exist and have a defined schema
table_id = ‘test_insert_nested
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref) # API requestrows_to_insert = [
 (“this_is_my_filename”, ‘2018–07–01 00:00:00’,\
 dict(some_number = 455, some_other_number= 6, some_float= 5.11))]
errors = client.insert_rows(table, rows_to_insert) 
print(errors)



from google.cloud import bigquery

bigquery_client = bigquery.Client()
table_id = 'myproject.mydataset.mytable'

# This example uses JSON, but you can use other formats.
# See https://cloud.google.com/bigquery/loading-data
job_config = bigquery.LoadJobConfig(
    source_format='NEWLINE_DELIMITED_JSON'
)

with open(source_file_name, 'rb') as source_file:
    job = bigquery_client.load_table_from_file(
        source_file, table_id, job_config=job_config
    )

job.result()  # Waits for the job to complete.
