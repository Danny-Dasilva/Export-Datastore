datastore export gs://bucket-name/Kind1 --project gcp-project --kinds Kind1


bq load --source_format=DATASTORE_BACKUP datastore_export.Kind1 gs://bucket-name/Kind1/default_namespace/kind_Kind1/default_namespace_kind_Kind1.export_metadata
