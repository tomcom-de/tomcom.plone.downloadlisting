#!/usr/bin/python
# -*- coding: utf-8 -*-

from tomcom.browser.public import *

class IDownloadListing(Interface):

    def get_latest(self):
        """ """

    def get_all(self,sort_on='getObjPositionInParent'):
        """ """

    def get_level(self,uid,portal_type):
        """ """

class Browser(BrowserView):

    implements(IDownloadListing)

    def get_latest(self):

        context=self.context
        pc=context.getAdapter('pc')()

        query={}
        query['portal_type']=['File','Image']
        query['path']=context.getPath()
        query['sort_on']='created'
        query['sort_order']='reverse'
        query['sort_limit']=5

        return pc(query)

    def get_all(self,sort_on='getObjPositionInParent',uid=None):

        context=self.context
        pc=context.getAdapter('pc')()

        query={}
        query['portal_type']=['File','Image']
        query['path']=context.getPath()
        query['sort_on']=sort_on

        if uid:
            getbrain=context.getAdapter('getbrain')
            brain=getbrain(uid)
            query['path']=brain.getPath()

        return pc(query)

    def get_level(self,uid,portal_type):

        context=self.context
        pc=context.getAdapter('pc')()
        getbrain=context.getAdapter('getbrain')
        brain=getbrain(uid)

        query={}
        query['path']={'query':brain.getPath(),
                       'depth':1}
        query['sort_on']='getObjPositionInParent'
        query['portal_type']=portal_type

        return pc(query)