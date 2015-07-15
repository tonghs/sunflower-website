$.fn.extend(
    uploader: (option) ->
        self = this
        if not self[0]
            return
        id = self[0].id
        if self[0].uploader
            return

        self[0].uploader = Qiniu.uploader
            runtimes: 'html5,html4,flash'    # 上传模式,依次退化
            browse_button: id       # 上传选择的点选按钮，**必需**
            uptoken_url: "/j/upload_token"            # Ajax请求upToken的Url，**必需**（服务端提供）
            domain: "#{CONST.QINIU_HOST}/"   # bucket 域名，下载资源时用到，**必需**
            max_file_size: option.max_file_size or '100mb'           # 最大文件体积限制
            #flash_swf_url : '/js/Moxie.swf'
            max_retries: 3                   # 上传失败最大重试次数
            dragdrop: true                   # 开启可拖曳上传
            drop_element: option.drop_element or null       # 拖曳上传区域元素的ID，拖曳文件或文件夹后可触发上传
            chunk_size: '4mb'                # 分块上传时，每片的体积
            auto_start: true                 # 选择文件后自动上传，若关闭需要自己绑定事件触发上传
            save_key: true
            filters: {
              mime_types : [
                option.mime_types or { title : "图片文件", extensions : "jpg,gif,png,bmp,jpeg" }
              ]
            }
            multi_selection: option.multi_selection or false
            init:
                'Error': (up, err, errTip) ->
                    option.error(up, err, errTip)
                'UploadProgress': (up, file) ->
                    option.uploading?.call(self,file.percent)
                    false
                'FileUploaded': (up, file, info) ->
                    domain = up.getOption('domain')
                    res = $.parseJSON(info)
                    id = res.key
                    url = domain + res.key # 获取上传成功后的文件的Url
                    fn = res.fn
                    option.uploaded?.call(self,id, url, res.fn, res)

    )
