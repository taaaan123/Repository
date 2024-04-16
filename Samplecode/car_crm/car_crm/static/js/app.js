 $(document).ready(function() {
    $(document).on('click', '.move-left', function(){
        let prev_car_order = $(this).parent().parent().prev().find('input').next().next().val()
        $(this).parent().children().next().next().next().val(parseInt(prev_car_order))
        // $(this).parent().submit()
    })
    $(document).on('click', '.move-right', function(){
        let next_car_order = $(this).parent().parent().next().find('input').next().next().val()
        $(this).parent().children().next().next().next().val(parseInt(next_car_order))
        // $(this).parent().submit()
    })
})