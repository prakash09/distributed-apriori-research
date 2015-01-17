StackExchange.postValidation=function(){function e(e,t,n,i){var r=e.find('input[type="submit"]:visible'),a=r.length&&r.is(":enabled");a&&r.attr("disabled",!0),o(e,i),s(e,t,n,i),c(e),u(e),h(e);var d=function(){1!=t||e.find(C).length?(l(e,i),a&&r.attr("disabled",!1)):setTimeout(d,250)};d()}function t(t,i,o,s,l){e(t,i,s,o);var c,u=function(e){if(e.success)if(l)l(e);else{var n=window.location.href.split("#")[0],r=e.redirectTo.split("#")[0];0==r.indexOf("/")&&(r=window.location.protocol+"//"+window.location.hostname+r),c=!0,window.location=e.redirectTo,n.toLowerCase()==r.toLowerCase()&&window.location.reload(!0)}else e.captchaHtml?e.nocaptcha?StackExchange.nocaptcha.init(e.captchaHtml,u):StackExchange.captcha.init(e.captchaHtml,u):e.errors?(t.find("input[name=priorAttemptCount]").val(function(e,t){return(+t+1||0).toString()}),p(e.errors,t,i,o,e.warnings)):t.find('input[type="submit"]:visible').parent().showErrorMessage(e.message)};t.submit(function(){if(t.find("#answer-from-ask").is(":checked"))return!0;var e=t.find(E);if("[Edit removed during grace period]"==$.trim(e.val()))return m(e,["Comment reserved for system use. Please use an appropriate comment."],d()),!1;if(a(),StackExchange.navPrevention&&StackExchange.navPrevention.stop(),t.find('input[type="submit"]:visible').parent().addSpinner(),StackExchange.helpers.disableSubmitButton(t),StackExchange.options.site.enableNewTagCreationWarning){var i=t.find(C).parent().find("input#tagnames"),s=i.prop("defaultValue");if(i.val()!==s)return $.ajax({"type":"GET","url":"/posts/new-tags-warning","dataType":"json","data":{"tags":i.val()},"success":function(e){n(e,t,c,o,u)}}),!1}return setTimeout(function(){r(t,o,c,u)},0),!1})}function n(e,t,n,a,o){if(e.showWarning){var s=$(e.html);s.bind("popupClose",function(){i(t,n)}),s.find(".popup-actions-cancel, .popup-close a").click(function(){StackExchange.helpers.closePopups(".popup"),i(t,n)}),s.find(".cancel-post").click(function(e){return StackExchange.helpers.closePopups(".popup"),e.preventDefault(),!1}),s.find(".submit-post").click(function(e){return StackExchange.helpers.closePopups(".popup"),r(t,a,n,o),e.preventDefault(),!1}),s.insertBefore(t.find('input[type="submit"]:visible')),StackExchange.helpers.bindMovablePopups(),s.show()}else r(t,a,n,o)}function i(e,t){StackExchange.helpers.removeSpinner(),t||StackExchange.helpers.enableSubmitButton(e)}function r(e,t,n,r){$.ajax({"type":"POST","dataType":"json","data":e.serialize(),"url":e.attr("action"),"success":r,"error":function(){var n;switch(t){case"question":n="An error occurred submitting the question.";break;case"answer":n="An error occurred submitting the answer.";break;case"edit":n="An error occurred submitting the edit.";break;case"tags":n="An error occurred submitting the tags.";break;case"post":default:n="An error occurred submitting the post."}e.find('input[type="submit"]:visible').parent().showErrorMessage(n)},"complete":function(){i(e,n)}})}function a(){for(var e=0;e<_.length;e++)clearTimeout(_[e]);_=[]}function o(e,t){var n=e.find(k);n.length&&n.blur(function(){_.push(setTimeout(function(){var i=n.val(),r=$.trim(i);if(0==r.length)return w(e,n),void 0;var a=n.data("min-length");if(a&&r.length<a)return m(n,[function(e){return 1==e.minLength?"Title must be at least "+e.minLength+" character.":"Title must be at least "+e.minLength+" characters."}({"minLength":a})],d()),void 0;var o=n.data("max-length");return o&&r.length>o?(m(n,[function(e){return 1==e.maxLength?"Title cannot be longer than "+e.maxLength+" character.":"Title cannot be longer than "+e.maxLength+" characters."}({"maxLength":o})],d()),void 0):($.ajax({"type":"POST","url":"/posts/validate-title","data":{"title":i},"success":function(i){i.success?w(e,n):m(n,i.errors.Title,d()),"edit"!=t&&g(e,n,i.warnings.Title)},"error":function(){w(e,n)}}),void 0)},A))})}function s(e,t,n,i){var r=e.find(S);r.length&&r.blur(function(){_.push(setTimeout(function(){var a=r.val(),o=$.trim(a);if(0==o.length)return w(e,r),void 0;if(5==t){var s=r.data("min-length");return s&&o.length<s?m(r,[function(e){return"Wiki Body must be at least "+e.minLength+" characters. You entered "+e.actual+"."}({"minLength":s,"actual":o.length})],d()):w(e,r),void 0}(1==t||2==t)&&$.ajax({"type":"POST","url":"/posts/validate-body","data":{"body":a,"oldBody":r.prop("defaultValue"),"isQuestion":1==t,"isSuggestedEdit":n},"success":function(t){t.success?w(e,r):m(r,t.errors.Body,d()),"edit"!=i&&g(e,r,t.warnings.Body)},"error":function(){w(e,r)}})},A))})}function l(e,t){var n=e.find(C);if(n.length){var i=n.parent().find("input#tagnames");i.blur(function(){_.push(setTimeout(function(){var r=i.val(),a=$.trim(r);return 0==a.length?(w(e,n),void 0):($.ajax({"type":"POST","url":"/posts/validate-tags","data":{"tags":r,"oldTags":i.prop("defaultValue")},"success":function(i){i.success?w(e,n):m(n,i.errors.Tags,d()),"edit"!=t&&g(e,n,i.warnings.Tags)},"error":function(){w(e,n)}}),void 0)},A))})}}function c(e){var t=e.find(E);t.length&&t.blur(function(){_.push(setTimeout(function(){var n=t.val(),i=$.trim(n);if(0==i.length)return w(e,t),void 0;var r=t.data("min-length");if(r&&i.length<r)return m(t,[function(e){return 1==e.minLength?"Your edit summary must be at least "+e.minLength+" character.":"Your edit summary must be at least "+e.minLength+" characters."}({"minLength":r})],d()),void 0;var a=t.data("max-length");return a&&i.length>a?(m(t,[function(e){return 1==e.maxLength?"Your edit summary cannot be longer than "+e.maxLength+" character.":"Your edit summary cannot be longer than "+e.maxLength+" characters."}({"maxLength":a})],d()),void 0):(w(e,t),void 0)},A))})}function u(e){var t=e.find(I);t.length&&t.blur(function(){_.push(setTimeout(function(){var n=t.val(),i=$.trim(n);if(0==i.length)return w(e,t),void 0;var r=t.data("min-length");if(r&&i.length<r)return m(t,[function(e){return"Wiki Excerpt must be at least "+e.minLength+" characters; you entered "+e.actual+"."}({"minLength":r,"actual":i.length})],d()),void 0;var a=t.data("max-length");return a&&i.length>a?(m(t,[function(e){return"Wiki Excerpt cannot be longer than "+e.maxLength+" characters; you entered "+e.actual+"."}({"maxLength":a,"actual":i.length})],d()),void 0):(w(e,t),void 0)},A))})}function h(e){var t=e.find(T);t.length&&t.blur(function(){_.push(setTimeout(function(){var n=t.val(),i=$.trim(n);return 0==i.length?(w(e,t),void 0):/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,20}$/i.test(n)?(w(e,t),void 0):(m(t,["This email does not appear to be valid."],f()),void 0)},A))})}function d(){var e=$("#sidebar, .sidebar").first().width()||270;return{"position":{"my":"left top","at":"right center"},"css":{"max-width":e,"min-width":e},"closeOthers":!1}}function f(){var e=$("#sidebar, .sidebar").first().width()||270;return{"position":{"my":"left top","at":"right center"},"css":{"min-width":e},"closeOthers":!1}}function p(e,t,n,i,r){if(e){var a=function(){var n=0,a=t.find(C),o=t.find(k),s=t.find(S);m(o,e.Title,d())?n++:w(t,o),r&&g(t,o,r.Title),m(s,e.Body,d())?n++:w(t,s),r&&g(t,s,r.Body),m(a,e.Tags,d())?n++:w(t,a),r&&g(t,a,r.Tags),m(t.find(E),e.EditComment,d())?n++:w(t,t.find(E)),m(t.find(I),e.Excerpt,d())?n++:w(t,t.find(I)),m(t.find(T),e.Email,f())?n++:w(t,t.find(T));var l=t.find(".general-error"),c=e.General&&e.General.length>0;if(c||n>0){if(!l.length){var u=t.find('input[type="submit"]:visible');u.before('<div class="general-error-container"><div class="general-error"></div><br class="cbt" /></div>'),l=t.find(".general-error")}if(c)m(l,e.General,{"position":"inline","css":{"float":"left","margin-bottom":"10px"},"closeOthers":!1,"dismissable":!1});else{w(t,l);var h;switch(i){case"question":h=function(e){return 1==e.specificErrorCount?"Your question couldn't be submitted. Please see the error above.":"Your question couldn't be submitted. Please see the errors above."}({"specificErrorCount":n});break;case"answer":h=function(e){return 1==e.specificErrorCount?"Your answer couldn't be submitted. Please see the error above.":"Your answer couldn't be submitted. Please see the errors above."}({"specificErrorCount":n});break;case"edit":h=function(e){return 1==e.specificErrorCount?"Your edit couldn't be submitted. Please see the error above.":"Your edit couldn't be submitted. Please see the errors above."}({"specificErrorCount":n});break;case"tags":h=function(e){return 1==e.specificErrorCount?"Your tags couldn't be submitted. Please see the error above.":"Your tags couldn't be submitted. Please see the errors above."}({"specificErrorCount":n});break;case"post":default:h=function(e){return 1==e.specificErrorCount?"Your post couldn't be submitted. Please see the error above.":"Your post couldn't be submitted. Please see the errors above."}({"specificErrorCount":n})}l.text(h)}}else t.find(".general-error-container").remove();var p;x()&&($("#sidebar").animate({"opacity":.4},500),p=setInterval(function(){x()||($("#sidebar").animate({"opacity":1},500),clearInterval(p))},500));var v;t.find(".validation-error").each(function(){var e=$(this).offset().top;(!v||v>e)&&(v=e)});var b=function(){for(var e=0;3>e;e++)t.find(".message").animate({"left":"+=5px"},100).animate({"left":"-=5px"},100)};if(v){var y=$(".review-bar").length;v=Math.max(0,v-(y?125:30)),$("html, body").animate({"scrollTop":v},b)}else b()},o=function(){1!=n||t.find(C).length?a():setTimeout(o,250)};o()}}function g(e,t,n){var i=d();if(i.type="warning",!n||0==n.length)return b(e,t),!1;var r=t.data("error-popup"),a=0;return r&&(a=r.height()+5),v(t,n,i,a)}function m(e,t,n){return n.type="error",v(e,t,n)}function v(e,t,n,i){var r,o=n.type;if(!(t&&0!=t.length&&e.length&&$("html").has(e).length))return!1;if(r=1==t.length?t[0]:"<ul><li>"+t.join("</li><li>")+"</li></ul>",r&&r.length>0){var s=e.data(o+"-popup");if(s&&s.is(":visible")){var l=e.data(o+"-message");if(l==r)return s.animateOffsetTop(i||0),!0;s.fadeOutAndRemove()}i>0&&(n.position.offsetTop=i);var c=StackExchange.helpers.showMessage(e,r,n);return c.find("a").attr("target","_blank"),c.click(a),e.addClass("validation-"+o).data(o+"-popup",c).data(o+"-message",r),!0}return!1}function b(e,t){y("warning",e,t)}function w(e,t){y("error",e,t)}function y(e,t,n){if(!n||0==n.length)return!1;var i=n.data(e+"-popup");return i&&i.is(":visible")&&i.fadeOutAndRemove(),n.removeClass("validation-"+e),n.removeData(e+"-popup"),n.removeData(e+"-message"),t.find(".validation-"+e).length||t.find(".general-"+e+"-container").remove(),!0}function x(){var e=!1,t=$("#sidebar, .sidebar").first();if(!t.length)return!1;var n=t.offset().left;return $(".message").each(function(){var t=$(this);return t.offset().left+t.outerWidth()>n?(e=!0,!1):void 0}),e}var k="input#title",S="textarea.wmd-input:first",C=".tag-editor",E="input[id^=edit-comment]",I="textarea#excerpt",T="input#m-address",_=[],A=250;return{"initOnBlur":e,"initOnBlurAndSubmit":t,"showErrorsAfterSubmission":p,"getSidebarPopupOptions":d}}();