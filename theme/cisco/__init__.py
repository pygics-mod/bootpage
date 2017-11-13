
import jinja2
from page import Static, W3
from bootpage import BootPageTheme

class Theme(BootPageTheme):
    def __init__(self,
                 logo='/page/bootpage/cisco/static/image/cisco_logo.png',
                 favicon='/page/bootpage/cisco/static/image/favicon.ico'):
        self.logo = logo
        self.favicon = favicon
        with open(pwd() + '/template.html') as fd: self.template = jinja2.Template(fd.read())
        Static('/page/bootpage/cisco/static', cache=False)
    
    def __import__(self, bootpage):
        bootpage._page_favicon = self.favicon
        bootpage.css(
            '/page/bootpage/cisco/static/css/icomoon.css',
            '/page/bootpage/cisco/static/css/cisco.css',
        )
        bootpage.js(
            '/page/bootpage/cisco/static/js/jquery-ui.min.js',
            '/page/bootpage/cisco/static/js/cisco.js',
        )
         
    def __render__(self, bootpage):
        bootpage.header(
            self.template.render({
                'url' : bootpage.url,
                'init' : bootpage._page_init,
                'title' : bootpage._page_title,
                'menu_list' : bootpage._bp_menu,
                'logo' : self.logo,
            })
        )
        bootpage.footer('</div>')

class Icon(W3.Span):
    def __init__(self, name, **attrs): W3.Span.__init__(self, **attrs); self.baseattr(Class='icon-asset icon-%s' % name)

class SideNavIcon(W3.Span):
    def __init__(self, name, **attrs): W3.Span.__init__(self, **attrs); self.baseattr(Class='sidenav-icon-asset icon-%s' % name)

