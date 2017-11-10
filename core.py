# -*- coding: utf-8 -*-
'''
Created on 2017. 11. 7.
@author: HyechurnJang
'''

import jinja2
from pygics import rest
from page import Page, Static, createVid

class Theme:
    
    def __import__(self, bootpage): pass
    def __render__(self, bootpage): pass

class BootPage(Page):
    
    def __init__(self,
                 url=None,
                 title='',
                 favicon='/page/static/image/favicon.ico',
                 static='static',
                 cache=True,
                 theme=None):
        Page.__init__(self, url, title, favicon, static, cache)
        
        class DefaultTheme(Theme):
            def __init__(self):
                with open(pwd() + '/theme/default.html') as fd: self.template = jinja2.Template(fd.read()) 
            def __render__(self, bootpage):
                bootpage.css('/page/bootpage/static/css/theme-default.css')
                bootpage.header(
                    self.template.render({
                        'url' : bootpage.url, 'title' : bootpage._page_title, 'menu_list' : bootpage._bp_menu
                    })
                )
        
        if theme != None: self._bp_theme = theme
        else: self._bp_theme = DefaultTheme()
        
        self.css(
            '/page/bootpage/static/css/bootstrap.min.css',
            '/page/bootpage/static/css/bootpage.css',
        )
        self.js(
            '/page/bootpage/static/js/popper.min.js',
            '/page/bootpage/static/js/bootstrap.min.js',
            '/page/bootpage/static/js/bootpage.js',
        )
        self._bp_theme.__import__(self)
        self._bp_menu = []
        self._bp_category = {}
    
    def menu(self, title, icon, **opts):
        
        def wrapper(func):
            id = createVid()
            name = func.__name__
            url = '%s/%s' % (self.url if self.url != '/' else '', name)
            desc = {'id' : id, 'name' : name, 'url' : url, 'title' : title, 'icon' : icon, 'type' : 'menu'}
            self._page_view[name] = desc
            self._bp_menu.append(desc)
            self._bp_theme.__render__(self)
            
            @rest('GET', url, **opts)
            def get(req, *argv, **kargs): return func(req, *argv, **kargs)
            
            @rest('POST', url, **opts)
            def post(req, *argv, **kargs): return func(req, *argv, **kargs)
             
            @rest('PUT', url, **opts)
            def put(req, *argv, **kargs): return func(req, *argv, **kargs)
             
            @rest('DELETE', url, **opts)
            def delete(req, *argv, **kargs): return func(req, *argv, **kargs)
            
            if self._page_init == '/page/empty':
                self._page_lock.on()
                self._page_init = url
                self._page_updated = True
                self._page_lock.off()
            
            return desc
        
        return wrapper
    
    def category(self, title, icon):
         
        def wrapper(desc):
            self._bp_menu.pop()
            if title not in self._bp_category:
                category = {'type' : 'category', 'title' : title, 'icon' : icon, 'submenu' : []}
                self._bp_category[title] = category
                self._bp_menu.append(category)
            else:
                category = self._bp_category[title]
            category['submenu'].append(desc)
            self._bp_theme.__render__(self)
         
        return wrapper

Static('/page/bootpage/static', cache=False)