
import jinja2
from page import Static, W3
from bootpage import BootPageTheme

class Theme(BootPageTheme):
    def __init__(self,
                 logo='/page/bootpage/cisco/static/image/cisco_logo.png',
                 favicon='/page/bootpage/cisco/static/image/favicon.ico',
                 wallpaper='/page/bootpage/cisco/static/image/wallpaper.jpg'):
        self.logo = logo
        self.favicon = favicon
        self.wallpaper = wallpaper
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
        if self.wallpaper != None:
            bootpage.head('''<style>
body { 
    background: url(%s) no-repeat center center fixed; 
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}
</style>''' % self.wallpaper)
         
    def __render__(self, bootpage):
        bootpage.header(
            self.template.render({
                'url' : bootpage.url,
                'init' : bootpage._page_init,
                'title' : bootpage._page_title,
                'menu_list' : bootpage._bp_menu,
                'logo' : self.logo
            })
        )
        bootpage.footer('</div>')

class MenuIcon(W3.Span):
    def __init__(self, name, **attrs): W3.Span.__init__(self, **attrs); self.baseattr(Class='sidenav-icon-asset icon-%s' % name)
