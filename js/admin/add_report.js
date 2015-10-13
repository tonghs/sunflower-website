// Generated by CoffeeScript 1.9.3
(function() {
  window.def_report = function(o) {
    if (o.img) {
      $('#img-preview').css('background-image', "url(" + CONST.QINIU_HOST + "/" + o.img + "?imageView2/1/w/436/h/436)");
      $('#img-preview').addClass('preview');
    }
    return def_view('ReportApp', 'ReportCtrl', function($scope) {
      $scope.o = o;
      $scope.percent = 0;
      return $scope.submit = function() {
        return $.postJSON('/j/admin/add_report', $scope.o, function(o) {
          return $.alert_success('保存成功', function() {
            return location.href = '/admin/reports';
          });
        });
      };
    });
  };

  $('#img_up').uploader({
    uploading: function(percent) {
      V().percent = percent;
      V().$apply();
      if (percent === 100) {
        return percent = 0;
      }
    },
    uploaded: function(id, url) {
      V().o.img = id;
      V().$apply();
      $('#img-preview').css('background-image', "url(" + url + "?imageView2/1/w/436/h/436)");
      return $('#img-preview').addClass('preview');
    },
    error: function(up, err, errTip) {
      return console.log(errTip);
    }
  });

}).call(this);