$("#deleteModal").on("show.bs.modal", function(event){
    var button = $(event.relatedTarget) 
    var modal = $(this)
    var id = button.data('id')
    var url = button.data('url')
    var placeholder = modal.find("#form-placeholder")
    placeholder.text("")
    var deletebtn = modal.find('#delete_btn')

    placeholder.html(`

        <form action="${url}" method="post" id="deleteForm">
            <input type="hidden" name="id" id="id" min=1 value="${id}">
        </form>
    `)

    deletebtn.click(function(){
        $("#deleteForm").submit()
    })

})
