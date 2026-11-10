var btnclick;

$(function () {
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

    $(".number[data-max]").keyup(function () {
        var max = parseFloat($(this).attr("data-max"));
        if ($(this).val() > max)
            $(this).val(max);
    });

    $('.datepicker').datetimepicker({
        format: 'DD-MM-YYYY',
        locale: 'id'
    });

    $('[data-toggle="tooltip"]').tooltip()

});

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
        bootbox.dialog({
            title: "Data Belum Lengkap",
            message: "Mohon mengisi isian yang bergaris merah",
            buttons: {
                success: {
                    label: "OK",
                    className: "btn-danger",
                    callback: function () {
                        error.focus();
                    }
                }
            }
        });
        error.focus();

        return false;
    } else
        return true;
}


function cekInputRequired(elem, eq) {
    var error = false;
    var target;

    target = $(elem).eq(eq - 1);

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
        bootbox.alert("Mohon mengisi isian yang bergaris merah");
        error.focus();

        return false;
    } else
        return true;
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
        } else if (!truetype) {
            bootbox.alert("File yang dapat diunggah hanya " + arrayoftype.join(", "));
            $(elm).val('');
        }
    }
}

function isInArray(value, array) {
    for (i = 0; i < array.length; i++) {
        if (array[i] == value) {
            return true;
        }
    }
    return false;
}

function focusElementOnError($element, $container) {
    if (!$container || !$container.length) {
        return;
    }

    $("html, body").animate({
        scrollTop: Math.max(0, $container.offset().top - 140)
    }, 200);

    if ($element && $element.length) {
        $element.focus();
    }
}

//mengatur tinggi kolom jalur pendaftaran agar sama
$( document ).ready(function() {
    var heights = $(".card-header").map(function() {
        return $(this).height();
    }).get(),

    maxHeight = Math.max.apply(null, heights);

    $(".card-header").height(maxHeight);
});
$( document ).ready(function() {
    var heights = $(".cards-jalur").map(function() {
        return $(this).height();
    }).get(),

    maxHeight = Math.max.apply(null, heights);

    $(".cards-jalur").height(maxHeight);
});