// Generated by CoffeeScript 1.9.3
(function() {
  $.fn.extend({
    uploader: function(option) {
      var id, self;
      self = this;
      if (!self[0]) {
        return;
      }
      id = self[0].id;
      if (self[0].uploader) {
        return;
      }
      return self[0].uploader = Qiniu.uploader({
        runtimes: 'html5,html4,flash',
        browse_button: id,
        uptoken_url: "/j/upload_token",
        domain: CONST.QINIU_HOST + "/",
        max_file_size: option.max_file_size || '100mb',
        max_retries: 3,
        dragdrop: true,
        drop_element: option.drop_element || null,
        chunk_size: '4mb',
        auto_start: true,
        save_key: true,
        filters: {
          mime_types: [
            option.mime_types || {
              title: "图片文件",
              extensions: "jpg,gif,png,bmp,jpeg"
            }
          ]
        },
        multi_selection: option.multi_selection || false,
        init: {
          'Error': function(up, err, errTip) {
            return option.error(up, err, errTip);
          },
          'UploadProgress': function(up, file) {
            var ref;
            if ((ref = option.uploading) != null) {
              ref.call(self, file.percent);
            }
            return false;
          },
          'FileUploaded': function(up, file, info) {
            var domain, fn, ref, res, url;
            domain = up.getOption('domain');
            res = $.parseJSON(info);
            id = res.key;
            url = domain + res.key;
            fn = res.fn;
            return (ref = option.uploaded) != null ? ref.call(self, id, url, res.fn, res) : void 0;
          }
        }
      });
    }
  });

}).call(this);
