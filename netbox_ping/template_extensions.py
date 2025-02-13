from netbox.plugins import PluginTemplateExtension

class PrefixExtension(PluginTemplateExtension):
    model = 'ipam.prefix'

    def buttons(self):
        prefix = self.context['object']
        return f'''
            <a href="/plugins/netbox_ping/ping-subnet/{prefix.id}/" class="btn btn-primary">
                <span class="mdi mdi-lan"></span>
                Ping Subnet
            </a>
        '''

template_extensions = [PrefixExtension] 