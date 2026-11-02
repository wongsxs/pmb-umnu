var btnclick, typeaheadt;

$(function () {
//    $('select').select2({theme: "bootstrap", 'dropdownAutoWidth': false});

    // load scroll
    $(window).scrollTop(localStorage.getItem("scroll"));
    localStorage.removeItem("scroll");
    
    
     $(".only-number").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110]) !== -1 ||
             // Allow: Ctrl+A, Command+A
            (e.keyCode === 65 && (e.ctrlKey === true || e.metaKey === true)) || 
             // Allow: home, end, left, right, down, up
            (e.keyCode >= 35 && e.keyCode <= 40)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });

    // number
    var decimal, separator;
    $(".number").each(function () {
       
        decimal = $(this).attr("data-decimal");
        if (decimal)
            decimal = parseInt(decimal);
        else
            decimal = 0;

        separator = $(this).attr("data-separator");
        if (separator)
            separator = '.';
        else
            separator = '';

        if ($(this).val())
            $(this).val($.number($(this).val(), decimal, ',', separator));
        else if ($(this).html())
            $(this).html($.number($(this).html(), decimal, ',', separator));

        if ($(this).is("input,textarea"))
            $(this).number(true, decimal, ',', separator);
    });

    $(".number[data-max]").keyup(function () {
        var max = parseFloat($(this).attr("data-max"));
        if ($(this).val() > max)
            $(this).val(max);
    });

    $(".number[data-min]").keyup(function () {
        var min = parseFloat($(this).attr("data-min"));
        if ($(this).val() < min)
            $(this).val(min);
    });


    // tanggal
   $('.datepicker').datetimepicker({
        format: 'DD-MM-YYYY',
        locale: 'id'
    });

    //$(".time").inputmask("hh:mm");

    /*$('.timepicker').timepicker({
     template: 'dropdown',
     appendWidgetTo: 'body',
     showSeconds: true,
     showMeridian: false,
     defaultTime: false,
     });*/

    // autocomplete
    $("[data-cari]").not(".tt-hint").each(function () {

        var inkey;
        var input = $(this);
        var parent = input.parent();
        var form = input.parents("form:eq(0)");
        var param = input.attr("data-param");
        var display = input.attr("data-display");
        var minsearch = input.attr("data-minsearch");
        var sugestion = input.attr("data-sugestion"); //add by dayat. untuk autocomplate yg sifatnya hanya sugestion

        //jika tidak ada defininisi, set 3 huruf untuk minimal search
        if (typeof minsearch == 'undefined')
            minsearch = 3;

        // cari key
        inkey = parent.find("[id='" + input.attr("data-inkey") + "']");
        if (inkey.length == 0)
            inkey = form.find("[id='" + input.attr("data-inkey") + "']");

        // buat url
        var url = input.attr("data-cari");

        // diberi typeahead
        if (input.is("input")) {
            var keyvallength = 0;
            input.typeahead({
                highlight: true,
                minLength: minsearch
            }, {
                source: function (query, process) {
                    if(typeaheadt)
                        clearTimeout(typeaheadt);

                    typeaheadt = setTimeout(function() {
                        return $.getJSON(g_abs_url + "ajax/" + url + getURLParam(parent, form, param) + "/" + query, function (data) {
                            if (sugestion && data.options.length == 0)
                                inkey.val(query); //set def. value from input by dayat
                            return process(data.options);
                        });
                    }, 300);
                }
            }).on('typeahead:queryChanged', function () {
                inkey.val("");
            }).on('typeahead:selected', function (ev, obj, ds) {
                inkey.val(obj.key);
                validate(inkey.attr("id"));
                keyvallength = obj.key.length;
            }).on('typeahead:autocompleted', function (ev, obj, ds) {
                inkey.val(obj.key);
            }).on('typeahead:blurred', function () {
                if (!inkey.val()){
                    if (display != "enable")
                        $(this).val("");
                    else
                        inkey.val($(this).val());
                }
            }).on('typeahead:closed', function (ev, obj, ds) {
                if(keyvallength == 0)
                    $(ev.currentTarget).val("");
            });
        }

        // jika sudah ada datanya
        if (input.attr("data-key")) {
            xhrfGetStr(url + getURLParam(parent, form, param) + "/" + input.attr("data-key") + "/1", function (data) {
                if (input.is("input"))
                    input.typeahead("val", data);
                else {
                    input.html(data);
                }
            });
        }
    });



    // disable button jika diclick
    $("button:not(.close)").bind("click", function () {
        btnclick = $(this);
    });

    // upload
    $(".input-foto").on('change', function () {
        goSubmit(this);
    });

    $(".select2").select2({
        theme: "bootstrap",
        dropdownAutoWidth: true,
        width: "100%",
      });

});

function resetAutoComplete() {

    // autocomplete
    $("[data-cari]").not(".tt-hint").each(function () {

        var inkey;
        var input = $(this);
        var parent = input.parent();
        var form = input.parents("form:eq(0)");
        var param = input.attr("data-param");
        var display = input.attr("data-display");
        var minsearch = input.attr("data-minsearch");
        var sugestion = input.attr("data-sugestion"); //add by dayat. untuk autocomplate yg sifatnya hanya sugestion

        //jika tidak ada defininisi, set 3 huruf untuk minimal search
        if (typeof minsearch == 'undefined')
            minsearch = 3;

        // cari key
        inkey = parent.find("[id='" + input.attr("data-inkey") + "']");
        if (inkey.length == 0)
            inkey = form.find("[id='" + input.attr("data-inkey") + "']");

        // buat url
        var url = input.attr("data-cari");

        // diberi typeahead
        if (input.is("input")) {
            input.typeahead({
                highlight: true,
                minLength: minsearch
            }, {
                source: function (query, process) {
                    return $.getJSON(g_abs_url + "ajax/" + url + getURLParam(parent, form, param) + "/" + query, function (data) {
                        return process(data.options);
                    });
                }
            }).on('typeahead:queryChanged', function () {
                inkey.val("");
            }).on('typeahead:selected', function (ev, obj, ds) {
                inkey.val(obj.key);
                validate(inkey.attr("id"))
            }).on('typeahead:autocompleted', function (ev, obj, ds) {
                inkey.val(obj.key);
            }).on('typeahead:blurred', function () {
                if (!inkey.val())
                    if (display != "enable") {
                        $(this).val("");
                    }
            });
        }

        // jika sudah ada datanya
        if (input.attr("data-key")) {
            xhrfGetStr(url + getURLParam(parent, form, param) + "/" + input.attr("data-key") + "/1", function (data) {
                if (input.is("input")){
                    input.typeahead("val", data);
                }else {
                    input.html(data);
                }
            });
        }
    });
}
function getURLParam(parent, form, param) {
    if (param) {
        var inparam;
        var url = "";
        var arrdata = new Array();
        var arrparam = param.split("/");

        for (i = 0; i < arrparam.length; i++) {
            arrdata[i] = arrparam[i];
            inparam = parent.find("[id='" + arrparam[i] + "']");
            if (inparam.length == 0)
                inparam = form.find("[id='" + arrparam[i] + "']");
            if (inparam.length > 0)
                arrdata[i] = inparam.val();
        }

        return "/" + arrdata.join("/");
    } else
        return ""; // string kosong
}

function getForm(elem) {
    elem = $(elem);

    if (elem.is("form"))
        return elem;
    else
        return elem.parents("form").eq(0);
}

function cekRequired(elem, tag) {
    var error = false;
    var target;

    if (tag)
        target = $(elem).parents(tag).eq(0);
    else
        target = getForm(elem);

    target.find(".required:not([readonly])").each(function () {
        var val = $(this).val();

        if (val != null) {
            val = val.trim();

            if (val.length == 0) {
                if (!error)
                    error = $(this);
                $(this).parent().addClass("has-error");
            } else
                $(this).parent().removeClass("has-error");
        }
    });

    if (error) {
        // bootbox.alert("Mohon mengisi isian yang bergaris merah");
        bootbox.alert({
            message: '<div class="content-confirmation"> <img src="'+url+'img/landing-page/icon-failed.svg" alt="failed"><div class="confirmation-message"><div class="title">Gagal Menyimpan Formulir</div><div class="description">mohon mengisi isian yang bergaris merah</div></div></div>',
            className: 'modal-confirmation',
            backdrop: true,
            centerVertical: true,
            buttons: {
                ok: {
                    label: "Ok",
                    className: 'button-pmb_primary'
                }
            }
        });
        error.focus();

        return false;
    } else
        return true;
}


function cekEmail(elem, tag) {
    var error = false;
    var target;

    if (tag)
        target = $(elem).parents(tag).eq(0);
    else
        target = getForm(elem);

    target.find(".email:not([readonly])").each(function () {
        if (!validateEmail($(this).val())) {
            if (!error)
                error = $(this);
            $(this).parent().addClass("has-error");
        } else
            $(this).parent().removeClass("has-error");
    });

    if (error) {
        bootbox.alert("Mohon gunakan format email yang tepat");
        error.focus();

        return false;
    } else
        return true;
}

function changeRole() {
    var data = $("#hakakses").val().split(":");

    location.href = home + "/change/" + data[0] + "/" + data[1];
}

function uploadFotoProfil() {
    $("#form_profil .input-foto").trigger('click');
}

function goSubmit(elem, act) {
    // simpan nilai scroll dulu
    localStorage.setItem("scroll", $(window).scrollTop());

    elem = $(elem); // diperlukan di bawah
    var form = getForm(elem);

    if (act)
        form.find("#act").val(act);

    // cek format laporan
    if ($("#format").length == 0 || $("#format").val() == "html") {
        if (elem.is("button") && !elem.is("[data-active]"))
            elem.prop("disabled", true);
        else if (btnclick && !btnclick.is("[data-active]"))
            btnclick.prop("disabled", true);
    }

    form.submit();
}

function goSubmitBlank(elem, page) {
    var form = getForm(elem);
    var action = form.attr("action");
    var target = form.attr("target");

    if (page)
        form.attr("action", g_abs_url + page);

    form.attr("target", "_blank");
    form.submit();

    if (action)
        form.attr("action", action);
    else
        form.removeAttr("action");

    if (target)
        form.attr("target", target);
    else
        form.removeAttr("target");
}

function countWords(str) {
    var i;
    var len = 0;
    var inc = true;
    var n = str.length;

    for (i = 0; i < n; i++) {
        if (str[i] == " ") {
            inc = true;
        } else if (inc) {
            len++;
            inc = false;
        }
    }

    return len;
}

$.expr[':'].iContains = function (n, i, m) {
    return jQuery(n).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
};

function validate(id) {
//    data = $("#form_data input,#form_data textarea, #form_data select").serialize();
//    data += "&field=" + $("#" + id).attr("name") + "&act=validate&key=" + (typeof key === 'undefined' ? "" : key);
//
//    $.ajax({
//        url: window.location.href,
//        type: "POST",
//        data: data,
//        success: function (result) {
//            data = JSON.parse(result);
//            $("#block-" + data.column).removeClass("has-error");
//            $("#block-" + data.column).removeClass("has-success");
//            $("#error-field-" + data.column).html("");
//
//            if (data.error) {
//                $("#block-" + data.column).addClass("has-error");
//                $("#error-field-" + data.column).html('<i class="fa fa-warning"></i> ' + data.message);
//            } else {
//                $("#block-" + data.column).addClass("has-success");
//            }
//        }
//    });
}


function printCharts(charts) {

    var origDisplay = [],
            origParent = [],
            body = document.body,
            childNodes = body.childNodes;

    // hide all body content
    Highcharts.each(childNodes, function (node, i) {
        if (node.nodeType === 1) {
            origDisplay[i] = node.style.display;
            node.style.display = "none";
        }
    });

    // put the charts back in
    $.each(charts, function (i, chart) {
        origParent[i] = chart.container.parentNode;
        body.appendChild(chart.container);
    });

    // print
    window.print();

    // allow the browser to prepare before reverting
    setTimeout(function () {
        // put the chart back in
        $.each(charts, function (i, chart) {
            origParent[i].appendChild(chart.container);
        });

        // restore all body content
        Highcharts.each(childNodes, function (node, i) {
            if (node.nodeType === 1) {
                node.style.display = origDisplay[i];
            }
        });
    }, 500);
}

function goPopup(elm) {
    popupPage = $(elm).attr("data-popup");
    popupVal = $("#" + $(elm).attr("id").replace("_label", "")).val();
    popupParam = $(elm).attr("data-param");
    $.ajax({
        method: "POST",
        url: popupPage,
        data: {selected: popupVal, param: popupParam, label: $(elm).attr("id").replace("_label", "")},
        success: function (data) {
            bootbox.dialog({
                message: data,
                size: "large",
                buttons: {
                    danger: {
                        label: "Tutup",
                        className: "btn-danger",
                        callback: function () {
                        }
                    },
                }
            });
        }
    });
}

function goPopupSave(key, subkey, page, titlePop) {
    $.ajax({
        method: "POST",
        url: page,
        data: {key: key, subkey: subkey},
        success: function (data) {
            bootbox.dialog({
                title: "<strong>" + titlePop + "</strong>",
                message: data,
                size: "large",
                buttons: {
                    success: {
                        label: "Simpan",
                        className: "btn-success simpan",
                        callback: function () {
                            goSavePop();
                            return false;
                        }
                    },
                    danger: {
                        label: "Tutup",
                        className: "btn-danger",
                        callback: function () {
                        }
                    },
                }
            });
        }
    });
}

function goSavePop() {
    formmodal = $("#form_modal");
    if (cekRequired(formmodal))
        goSubmit(formmodal, "savepop");
}

function goFileCheck(elm) {
    var filesize = $(elm)[0].files[0].size;
    var filename = $(elm)[0].files[0].name;
    var filetype = filename.split('.').pop().toLowerCase();

    var typerule = $(elm).attr('filetype');
    var arrayoftype = typerule.split('::');
    var sizerule = $(elm).attr('maxsize');

    var truetype = isInArray(filetype, arrayoftype);
    if (typerule != "") {
        if (filesize > sizerule) {
            let maxSizeMessage = (sizerule / 1000000) < 1
                ? (sizerule / 1024) + " KB"
                : (sizerule / 1000000) + " MB";
            bootbox.alert("Ukuran file terlalu besar, maksimal " + maxSizeMessage);
            $(elm).val('');
        } else if (truetype) {
            bootbox.alert("File yang dapat diunggah hanya " + arrayoftype.join(", "));
            $(elm).val('');
        }
    }
}

function isInArray(value, array) {
    return array.indexOf(value) <= -1;
}

function goClockMode(elm) {
    $(elm).mask("99:99", {placeholder: "hh:mm"});
}
