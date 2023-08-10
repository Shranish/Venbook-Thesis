from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'venbookstorage' # Must be replaced by your <storage_account_name>
    account_key = 'i4mTVr3qAhdqQKlmin+VIhwUJtjTyLDDNmb+o3ALSeQXbV8LAOsbPVVVaazynr1mfvReN2GL2PPL+AStuXjfKg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'venbookstorage' # Must be replaced by your storage_account_name
    account_key = 'i4mTVr3qAhdqQKlmin+VIhwUJtjTyLDDNmb+o3ALSeQXbV8LAOsbPVVVaazynr1mfvReN2GL2PPL+AStuXjfKg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None