$(document).ready(function(){
  var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
  
  // when the button clicked
  $("#createButton").click(function(){
    // grap the passed data and the csrf 
    var serializedData = 
    $("#createTaskForm").serialize();
    // console.log(serializedData)

    $.ajax({
      // grap the url from the form 
      url: $("createTaskForm").data('url'),
      data: serializedData,
      type: 'post',
      success: function(response){
        //  inject the newly created task in the body layout
        $("#taskList").append(
        '<div class="card mb-1" id="taskCard" data-id="'+ response.task.id+'"><div class="card-body">'+ response.task.title +'<button type="button" class="close float-right"data-id="'+response.task.id+'"><span aria-hidden="true">&times;</span></button></div></div>')
      }
    })
    $("#createTaskForm")[0].reset();
  });
  // when click on any div with card class execute the function
  $("#taskList").on('click','.card',function(){
    // refer to the particluar card and grap the id from the data
    var dataId = $(this).data('id');
    $.ajax({
      data :{
      url : '/tasks/'+dataId+'/comleted/',
      csrfmiddlewaretoken : csrfToken,
      id : dataId
      },
      type : 'post',
      success : function(){
        var cardItem = $('#taskCard[data-id="'+dataId+'"]');
        cardItem.css('text-decoration','line-through').hide().slideDown();
        $("#taskList").append(cardItem);
      }
    });
    // button with close class
  }).on('click','button.close',function(event){
    // don't extend the event to the element parent
    event.stopPropagation();
    var dataId = $(this).data('id');
    $.ajax({
      url : '/tasks/'+dataId+'/delete/',
      data :{
        csrfmiddlewaretoken : csrfToken,
        id : dataId
      },
      type: 'post',
      dataType: 'json',
      success: function(){
        $('#taskCard[data-id="'+dataId+'"]').remove();
      }
  });
});
})
