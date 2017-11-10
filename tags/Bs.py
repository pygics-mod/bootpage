# -*- coding: utf-8 -*-
'''
Created on 2017. 11. 8.
@author: HyechurnJang
'''

from page import W3, createVid

class Util:
    
    class Float:
        ClearFix = {'class' : 'clearfix'}
        Left = {'class' : 'float-left'}
        Right = {'class' : 'float_right'}
    
    class Bg:
        Primary = {'class' : 'bg-primary'}
        Secondary = {'class' : 'bg-secondary'}
        Success = {'class' : 'bg-success'}
        Danger = {'class' : 'bg-danger'}
        Warning = {'class' : 'bg-warning'}
        Info = {'class' : 'bg-info'}
        Light = {'class' : 'bg-light'}
        Dark = {'class' : 'bg-dark'}
        White = {'class' : 'bg-white'}
        Transparent = {'class' : 'bg-transparent'}
    
    class Border:
        Primary = {'class' : 'border border-primary'}
        Secondary = {'class' : 'border border-secondary'}
        Success = {'class' : 'border border-success'}
        Danger = {'class' : 'border border-danger'}
        Warning = {'class' : 'border border-warning'}
        Info = {'class' : 'border border-info'}
        Light = {'class' : 'border border-light'}
        Dark = {'class' : 'border border-dark'}
        White = {'class' : 'border border-white'}
    
    class Text:
        Primary = {'class' : 'text-primary'}
        Secondary = {'class' : 'text-secondary'}
        Success = {'class' : 'text-success'}
        Danger = {'class' : 'text-danger'}
        Warning = {'class' : 'text-warning'}
        Info = {'class' : 'text-info'}
        Light = {'class' : 'text-light'}
        Dark = {'class' : 'text-dark'}
        Muted = {'class' : 'text-muted'}
        White = {'class' : 'text-white'}
        
        Left = {'class' : 'text-left'}
        Center = {'class' : 'text-center'}
        Right = {'class' : 'text-right'}
        
        Top = {'class' : 'align-top'}
        Middle = {'class' : 'align-middle'}
        Bottom = {'class' : 'align-bottom'}
        
        Wrap = {'class' : 'text-truncate'}
        NoWrap = {'class' : 'text-nowrap'}
        
        Bold = {'class' : 'font-weight-bold'}
        Normal = {'class' : 'font-weight-normal'}
        light = {'class' : 'font-weight-light'}
        italic = {'class' : 'font-weight-italic'}
        
    class Rounded:
        All = {'class' : 'rounded'}
        Top = {'class' : 'rounded-top'}
        Bottom = {'class' : 'rounded-bottom'}
        Left = {'class' : 'rounded-left'}
        Right = {'class' : 'rounded-right'}
        Circle = {'class' : 'rounded-circle'}
        No = {'class' : 'rounded-0'}
    
    @classmethod
    def margin(cls, size, side=None):
        return {'class' : 'm%s-%s' % (str(side), size) if side else 'm-%s' % str(size)}
    
    @classmethod
    def padding(cls, size, side=None):
        return {'class' : 'p%s-%s' % (str(side), size) if side else 'p-%s' % str(size)}
    
class Container(W3.Div):
    def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='container')

class ContFluid(W3.Div):
    def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='container-fluid')

class Row(W3.Div):
    def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='row')

class Col(W3.Div):
    def __init__(self, size, scr=None, **attrs): W3.Div__init__(self, **attrs); self.baseattr(Class='col-%s-%d' % (scr, size) if scr else 'col-%d' % size)
    
    XSMALL = None
    SMALL = 'sm'
    MIDIUM = 'md'
    LARGE = 'lg'
    XLARGE = 'xl'

class Flex(W3.Div):
    def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='d-flex')

    Row = {'class' : 'flex-row'}
    RowRev = {'class' : 'flex-row-reverse'}
    Col = {'class' : 'flex-column'}
    ColRev = {'class' : 'flex-column-reverse'}
    Wrap = {'class' : 'flex-wrap'}
    NoWrap = {'class' : 'flex-nowrap'}
    
    class Align:
        
        class Horizonal:
            Start = {'class' : 'justify-content-start'}
            End = {'class' : 'justify-content-end'}
            Center = {'class' : 'justify-content-center'}
            Between = {'class' : 'justify-content-between'}
            Around = {'class' : 'justify-content-around'}
            
        class Vertical:
            Start = {'class' : 'align-items-start'}
            End = {'class' : 'align-items-end'}
            Center = {'class' : 'align-items-center'}
            Baseline = {'class' : 'align-items-baseline'}
            Stretch = {'class' : 'align-items-stretch'}
        
        class Wrap:
            Start = {'class' : 'align-content-start'}
            End = {'class' : 'align-content-end'}
            Center = {'class' : 'align-content-center'}
            Between = {'class' : 'align-content-between'}
            Around = {'class' : 'align-content-around'}
            Stretch = {'class' : 'align-content-stretch'}

class Alert(W3.Div):
    def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='alert alert-dismissible fade show', Role='alert')
    
    Primary = {'class' : 'alert-primary'}
    Secondary = {'class' : 'alert-secondary'}
    Success = {'class' : 'alert-success'}
    Danger = {'class' : 'alert-danger'}
    Warning = {'class' : 'alert-warning'}
    Info = {'class' : 'alert-info'}
    Light = {'class' : 'alert-light'}
    Dark = {'class' : 'alert-dark'}
    
    class H(W3.H):
        def __init__(self, level, **attrs): W3.H.__init__(self, level, **attrs); self.baseattr(Class='alert-heading')
    
    class Dismiss(W3.Button):
        def __init__(self, **attrs):
            W3.Button.__init__(self, **attrs)
            self.baseattr(**{'type' : 'button', 'class' : 'close', 'data-dismiss' : 'alert', 'aria-label' : 'Close'})
            self.html(W3.Span(**{'aria-hidden' : 'true'}).html('&times;'))

class Badge(W3.Span):
    def __init__(self, **attrs): W3.Span.__init__(self, **attrs); self.baseattr(Class='badge')
    
    Primary = {'class' : 'badge-primary'}
    Secondary = {'class' : 'badge-secondary'}
    Success = {'class' : 'badge-success'}
    Danger = {'class' : 'badge-danger'}
    Warning = {'class' : 'badge-warning'}
    Info = {'class' : 'badge-info'}
    Light = {'class' : 'badge-light'}
    Dark = {'class' : 'badge-dark'}
    
class BreadCrumb(W3.Nav):
    def __init__(self, **attrs):
        W3.Nav.__init__(self, **attrs)
        self.baseattr(**{'aria-label' : 'breadcrumb', 'role' : 'navigation'})
        self._breadcrumb_ol = W3.Ol(Class='breadcrumb')
        self._breadcrumb_active = None
        self['elems'].append(self._breadcrumb_ol)
    
    def html(self, *elems):
        elem = None
        for elem in elems: self._breadcrumb_ol.append(elem)
        if elem != None:
            if self._breadcrumb_active != None:
                self._breadcrumb_active['class'] = self._breadcrumb_active['class'].remove(' active')
                self._breadcrumb_active.pop('aria-current')
            elem.attr(**{'class' : 'active', 'aria-current' : 'page'})
            self._breadcrumb_active = elem['attrs']
        return self
    
    class Item(W3.Li):
        def __init__(self, **attrs): W3.Li.__init__(self, **attrs); self.baseattr(Class='breadcrumb-item')

class Button(W3.Button):
    def __init__(self, **attrs): W3.Button.__init__(self, **attrs); self.baseattr(Type='button', Class='btn')
    
    Primary = {'class' : 'btn-primary'}
    Secondary = {'class' : 'btn-secondary'}
    Success = {'class' : 'btn-success'}
    Danger = {'class' : 'btn-danger'}
    Warning = {'class' : 'btn-warning'}
    Info = {'class' : 'btn-info'}
    Light = {'class' : 'btn-light'}
    Dark = {'class' : 'btn-dark'}
    Link = {'class' : 'btn-link'}
    
    Large = {'class' : 'btn-lg'}
    Small = {'class' : 'btn-sm'}
    Block = {'class' : 'btn-block'}
    
    class Outline:
        Primary = {'class' : 'btn-outline-primary'}
        Secondary = {'class' : 'btn-outline-secondary'}
        Success = {'class' : 'btn-outline-success'}
        Danger = {'class' : 'btn-outline-danger'}
        Warning = {'class' : 'btn-outline-warning'}
        Info = {'class' : 'btn-outline-info'}
        Light = {'class' : 'btn-outline-light'}
        Dark = {'class' : 'btn-outline-dark'}
    
    #===========================================================================
    # Grouping
    #===========================================================================
    class ToolBar(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='btn-toolbar', Role='toolbar')
    
    class Group(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='btn-group', Role='group')
        
        Large = {'class' : 'btn-group-lg'}
        Small = {'class' : 'btn-group-sm'}
        Vertical = {'class' : 'btn-group-vertical'}
    
class Card(W3.Div):
    def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card')
    
    class Header(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card-header')
    
    class Body(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card-body')
    
    class Footer(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card-footer')
    
    class Title(W3.H):
        def __init__(self, level, **attrs): W3.H.__init__(self, level, **attrs); self.baseattr(Class='card-title')
    
    class SubTitle(W3.H):
        def __init__(self, level, **attrs): W3.H.__init__(self, level, **attrs); self.baseattr(Class='card-subtitle')
    
    class Text(W3.P):
        def __init__(self, **attrs): W3.P.__init__(self, **attrs); self.baseattr(Class='card-text')
    
    class Link(W3.A):
        def __init__(self, **attrs): W3.A.__init__(self, **attrs); self.baseattr(Class='card-link')
    
    class Img(W3.Img):
        def __init__(self, src, locate=None, **attrs): W3.Img.__init__(self, **attrs); self.baseattr(Class='card-img-%s' % locate if locate else 'card-img', Src=src)
        
        Top = 'top'
        Bottom = 'bottom'
    
    class Overlay(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card-img-overlay')
    
    #===========================================================================
    # Grouping
    #===========================================================================
    class Group(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card-group')
    
    class Deck(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card-deck')
    
    class Columns(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='card-columns')

class Carousel(W3.Div):
    
    def __init__(self, prev=Carousel.Prev(), next=Carousel.Next(), indicator=Carousel.Indicator(), **attrs):
        W3.Div.__init__(self, **attrs)
        self._carousel_id = createVid()
        self.baseattr(**{'id' : self._carousel_id, 'class' : 'carousel slide', 'data-ride' : 'carousel'})
        self._carousel_indicator = indicator
        self._carousel_count = 0
        self._carousel_inner = W3.Div(Class='carousel-inner')
        if indicator != None: self['elems'].append(self._carousel_indicator)
        self['elems'].append(self._carousel_inner)
        if prev != None: self['elems'].append(prev.attr(Href='#' + self._carousel_id))
        if next != None: self['elems'].append(next.attr(Href='#' + self._carousel_id))
    
    def html(self, *elems):
        for elem in elems:
            if not self._carousel_inner:
                self._carousel_inner.html(elem)
                if self._carousel_indicator != None:
                    self._carousel_indicator.html(W3.Li(**{'data-target' : '#' + self._carousel_id, 'data-slide-to' : '%d' % self._carousel_count}))
            else:
                self._carousel_inner.html(elem.attr(Class='active'))
                if self._carousel_indicator != None:
                    self._carousel_indicator.html(W3.Li(**{'class' : 'active', 'data-target' : '#' + self._carousel_id, 'data-slide-to' : '%d' % self._carousel_count}))
        return self
    
    class Prev(W3.A):
        def __init__(self, **attrs):
            W3.A.__init__(self, **attrs)
            self.baseattr(**{'class' :'carousel-control-prev', 'role' : 'button', 'data-slide' : 'prev'})
            self.html(W3.Span(**{'class' : 'carousel-control-prev-icon', 'aria-hidden' : 'true'}))
    
    class Next(W3.A):
        def __init__(self, **attrs):
            W3.A.__init__(self, **attrs)
            self.baseattr(**{'class' :'carousel-control-next', 'role' : 'button', 'data-slide' : 'next'})
            self.html(W3.Span(**{'class' : 'carousel-control-next-icon', 'aria-hidden' : 'true'}))
    
    class Indicator(W3.Ol):
        def __init__(self, **attrs): W3.Ol.__init__(self, **attrs); self.baseattr(Class='carousel-indicators')
    
    class Item(W3.Div):
        def __init__(self, src, **attrs):
            W3.Div.__init__(self, **attrs);
            self.baseattr(Class='carousel-item')
            self.html(W3.Img(Src=src))
                
    class Caption(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='carousel-caption')

class Collapse(W3.Div):
    def __init__(self, expanded=False, **attrs):
        W3.Div.__init__(self, **attrs)
        self._collapse_id = createVid()
        self.baseattr(Id=self._collapse_id, Class='collapse show' if expanded else 'collapse')
        self._event_attr = {
            'data-toggle' : 'collapse',
            'data-target' : '#%s' % self._collapse_id,
            'href' : '#%s' % self._collapse_id,
            'aria-expanded' : 'true' if expanded else 'false',
            'aria-controls' : self._collapse_id
        }
    
    def event(self): return self._event_attr

class Accordion(W3.Div):
    def __init__(self, **attrs):
        W3.Div.__init__(self, **attrs)
        self._accordion_id = createVid()
        self.baseattr(Id=self._accordion_id)
        self._accordion_items = {}
    
    def __create_item__(self, num, expanded):
        if num not in self._accordion_items:
            collapse_id = '%s-%s' % (self._collapse_id, num)
            self._accordion_items[num] = {
                'event' : {
                    'data-toggle' : 'collapse',
                    'data-target' : '#%s' % collapse_id,
                    'href' : '#%s' % collapse_id,
                    'aria-expanded' : 'true' if expanded else 'false',
                    'aria-controls' : collapse_id
                },
                'data' : {
                    'id' : collapse_id,
                    'class' : 'collapse show' if expanded else 'collapse',
                    'data-parent' : '#%s' % self._accordion_id
                }
            }
    
    def event(self, num, expanded=False):
        num = str(num)
        self.__create_item__(num, expanded)
        return self._accordion_items[num]['event']
    
    def data(self, num, expanded=False):
        num = str(num)
        self.__create_item__(num, expanded)
        return self._accordion_items[num]['data']

class DropDown(W3.Div):
    def __init__(self, button=Button(), **attrs):
        W3.Div.__init__(self, **attrs)
        self.baseattr(Class='dropdown')
        button.attr(**{'class' : 'dropdown-toggle', 'data-toggle' : 'dropdown', 'aria-haspopup' : 'true', 'aria-expanded' : 'false'})
        self['elems'].append(button)
        self._dropdown_menu = W3.Div(Class='dropdown-menu')
        self['elems'].append(self._dropdown_menu)
    
    def html(self, *elems):
        self._dropdown_menu.html(*elems)
        return self
    
    class Item(W3.A):
        def __init__(self, **attrs): W3.A.__init__(self, **attrs); self.baseattr(Class='dropdown-item')
        
        Disabled = {'class' : 'disabled'}
    
    class Header(W3.H):
        def __init__(self, level, **attrs): W3.H.__init__(self, level, **attrs); self.baseattr(Class='dropdown-header')
    
    class Divider(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='dropdown-divider')
        
class Forms:
    
    class Input(W3.Input):
        def __init__(self, type, **attrs): W3.Input.__init__(self, **attrs); self.baseattr(Type=type, Class='form-control')
    
    class Label(W3.Label):
        def __init__(self, size=None, **attrs): W3.Label.__init__(self, **attrs); self.baseattr(Class='col-form-label-%s' % size if size else 'col-form-label')
        
        Large = 'lg'
        Small = 'sm'
    
    class Text(Forms.Input):
        def __init__(self, **attrs): Forms.Input.__init__(self, 'text', **attrs)
    
    class Password(Forms.Input):
        def __init__(self, **attrs): Forms.Input.__init__(self, 'password', **attrs)
    
    class Email(Forms.Input):
        def __init__(self, **attrs): Forms.Input.__init__(self, 'email', **attrs); self.attr(PlaceHolder='name@example.com')
    
    class File(Forms.Input):
        def __init__(self, **attrs): Forms.Input.__init__(self, 'file', **attrs)
    
    class TextArea(W3.TextArea):
        def __init__(self, **attrs): W3.TextArea.__init__(self, **attrs); self.baseattr(Class='form-control')
    
    class Select(W3.Select):
        def __init__(self, multiple=False, **attrs):
            W3.Select.__init__(self, **attrs)
            if multiple: self.baseattr(Class='form-control', Multiple='true')
            else: self.baseattr(Class='form-control')
        
    class Check(W3.Div):
        def __init__(self, tag, inline=False, **attrs):
            W3.Div.__init__(self, Class='form-check form-check-inline' if inline else 'form-check')
            self._radio_label = W3.Label(**attrs).baseattr(Class='form-check-label').html(tag)
            self['elems'].append(self._radio_label)
        
        def attr(self, **attrs):
            own_attrs = self._radio_label['attrs']
            for key, val in attrs.items():
                key_low = key.lower()
                own_attrs[key_low] = '%s %s' % (own_attrs[key_low], val) if key_low in own_attrs else val
            return self
        
        def baseattr(self, **attrs):
            own_attrs = self._radio_label['attrs']
            for key, val in attrs.items():
                key_low = key.lower()
                own_attrs[key_low] = '%s %s' % (val, own_attrs[key_low]) if key_low in own_attrs else val
            return self
        
        def html(self, *elems):
            self._radio_label.html(*elems)
            return self
        
    class CheckBox(W3.Input):
        def __init__(self, **attrs): W3.Input.__init__(self, **attrs); self.baseattr(Type='checkbox', Class='form-check-input', Value='')
        
    class Radio(W3.Input):
        def __init__(self, name, **attrs): W3.Input.__init__(self, **attrs); self.baseattr(Type='radio', Class='form-check-input', Name=name, Value='')
        
        Inline = {'inline' : True}
    
    Large = {'class' : 'form-control-lg'}
    Small = {'class' : 'form-control-sm'}
    
    ReadOnly = {'readonly' : 'true'}
    PlainText = {'class' : 'form-control-plaintext', 'readonly' : 'true'}
    
    Valid = {'class' : 'is-valid'}
    Invalid = {'class' : 'is-invalid'}
    
    class Group(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='form-group')
    
    class Row(W3.Div):
        def __init__(self, **attrs): W3.Div.__init__(self, **attrs); self.baseattr(Class='form-row')















