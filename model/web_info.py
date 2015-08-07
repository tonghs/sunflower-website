#!/usr/bin/env python
#coding: utf-8

import _env
from db import Doc
from config import HOST

class WebInfo(Doc):
    structure = dict(
        id_ = int,
        home_img = basestring,
        program_img = basestring,

        phone = basestring,
        email = basestring,
        location = basestring,

        weixin = basestring,
        program_weixin = basestring,
        weibo = basestring,

        logo = basestring,
        desc = basestring,
        program = basestring,
        founder_img = basestring
    )

    indexes = [
        { 'fields': ['id_'] },
    ]

    @classmethod
    def web_info_upsert(cls, doc, id_=1):
        o = WebInfo(doc)
        o.upsert(dict(id_=id_))

    def web_info_get(cls, html=False, id_=1):
        o = WebInfo.find_one(dict(id_=id_))
        if html:
            desc = o.desc.replace('>', '&gt;').replace('<', '&lt;').replace('\n', '</p><p class="s-font">')

            o.desc = '<p class="s-font">%s</p>' % desc

            program = o.program.replace('>', '&gt;').replace('<', '&lt;').replace('\n', '</p><p class="s-font">')

            o.program = '<p class="s-font">%s</p>' % program

        return o


if __name__ == "__main__":

    doc = dict(
        id_ = 1,
        home_img = 'http://www.uniqueway.com/assets/welcome/welcome_banner-29b0aa78eac9329b9d505c377a994c14.jpg',
        program_img = 'http://7xk1xj.com1.z0.glb.clouddn.com/img/program.png',

        phone = '010-53670611',
        email = 'sunflower@xrkmedia.com',
        location = '北京市朝阳区阜安西路望京soho塔2-B座-1802',

        weixin = 'tonghuashuai',
        weibo = 'http://weibo.com',

        logo = 'https://7xk1xj.com1.z0.glb.clouddn.com/img/logo-white.png',
        desc = '''由山东德兴集团、永安信控股和资深媒体人 共同建立的文化金融传媒机构.坐落于北京望京SOHO，注册资本5000万。
        作为现时代金融文化产品提供机构，我们致力于将中国优秀文化产品与金融服务相结合， 打造传媒与金融相结合的投融资服务平台；我们已聚合天使街、黑马会、天使汇、首都金融服务商会等多家金融投资机构， 真实呈现全民创投的热潮，打造线上线下金融超市；向日葵传媒已经发起种子基金计划， 为有优质创业项目的80、90后提供100——200万元的项目启动基金。
        同时，我们将借力互联网+的浪潮，吸纳最前沿的科技，开拓全新的TV 2 online形态 提升传统电视平台与wap、app端新媒体的粘性， 让观众在观看节目的同时参与到丰富多彩的互动。''',
        founder = '创始人简介',
        founder_img = 'https://7xk1xj.com1.z0.glb.clouddn.com/img/founder.png?imageMogr2/thumbnail/600x' 
    )
    WebInfo.web_info_upsert(doc)
    pass

