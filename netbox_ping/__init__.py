from netbox.plugins import PluginConfig

class Config(PluginConfig):
    name = 'netbox_ping'
    verbose_name = 'NetBox Ping'
    description = 'Ping IPs and subnets'
    version = '0.2'
    author = 'Christian Rose'
    default_settings = {
        'exclude_virtual_interfaces': True
    }

    # Register the custom table
    ipaddress_table = 'netbox_ping.tables.CustomIPAddressTable'
    
    # Define which models support custom fields
    custom_field_models = ['ipaddress']

config = Config