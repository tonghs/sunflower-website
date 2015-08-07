// Generated by CoffeeScript 1.4.0
(function() {
  var pathname;

  $.fn.extend({
    parallax: function() {
      var ratio, scroll_top, self;
      scroll_top = $(window).scrollTop();
      self = $(this);
      ratio = parseFloat(self.data('parallax-background-ratio'));
      return self.css('background-position', "center " + (scroll_top * ratio) + "px");
    }
  });

  $('.to-top').click(function() {
    return $("html,body").animate({
      scrollTop: $("#top").offset().top - 100
    }, 500);
  });

  $("#footer-sns #weixin").poshytip({
    className: 'tip-twitter',
    alignTo: 'target',
    alignX: 'center'
  });

  pathname = location.pathname;

  $("#navbar>ul>li").removeClass('active');

  $("#navbar>ul>li").each(function() {
    var self;
    self = $(this);
    if (self.children("a").attr('href') === pathname) {
      return self.addClass('active');
    }
  });

  window.def_view = function(module, ctrl, fun) {
    var app;
    app = angular.module(module, ["ngSanitize"]).controller(ctrl, fun);
    app.filter('deal_str', function() {
      return $.deal_str;
    });
    window.V = function() {
      return angular.element($("[ng-controller=" + ctrl + "]")).scope();
    };
    return app;
  };

  $(".nav>li").removeClass('active');

  $(".nav>li").each(function() {
    var self;
    self = $(this);
    if (self.children("a").attr('href') === pathname) {
      return self.addClass('active');
    }
  });

  $('.table-expandable>tbody>tr>td>a.open').click(function() {
    var obj;
    obj = $(this).parent('td').parent('tr').next();
    if (obj.attr('class') && obj.attr('class').indexOf('collapse') >= 0) {
      if (obj.css('display') === 'none') {
        return obj.slideDown();
      } else {
        return obj.slideUp(0);
      }
    }
  });

  $.postJSON = function(url, data, callback) {
    return $.ajax({
      url: url,
      data: data,
      type: 'post',
      success: function(o) {
        if (o.err) {
          return $.alert_fail(o.err.msg);
        } else {
          return callback(o);
        }
      },
      error: function(o) {
        return $.alert_fail();
      }
    });
  };

  $.deal_str = function(str) {
    var r;
    r = new RegExp('>', 'g');
    str = str.replace(r, '&gt;');
    r = new RegExp('<', 'g');
    str = str.replace(r, '&lt;');
    str = str.replace(/\n/g, "</p><p>");
    return "<p>" + str + "</p>";
  };

  $.alert_success = function(msg, callback) {
    var dialog;
    if (msg == null) {
      msg = '操作成功';
    }
    dialog = BootstrapDialog.show({
      title: '提示',
      type: 'type-success',
      message: msg,
      buttons: [
        {
          label: '关闭',
          action: function(dialogItself) {
            return dialogItself.close();
          }
        }
      ],
      onhidden: function() {
        if (callback) {
          return callback();
        }
      }
    });
    return setTimeout(function() {
      return dialog.close();
    }, 2000);
  };

  $.alert_fail = function(msg) {
    var dialog;
    if (msg == null) {
      msg = '操作失败';
    }
    return dialog = BootstrapDialog.show({
      title: '提示',
      type: 'type-danger',
      message: msg,
      buttons: [
        {
          label: '关闭',
          action: function(dialogItself) {
            return dialogItself.close();
          }
        }
      ],
      onhidden: function() {
        if (callback) {
          return callback();
        }
      }
    });
  };

}).call(this);
