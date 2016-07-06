$(document).ready(function(){
	/*******    ↓製作隱藏側欄的功能↓   *******/
	/***all booklist toggle***/
	$('#toggle_list').click(function(){
		//$('#bulletin').slideToggle();
		$('#bulletin').toggle("slow");//you can choose the special effect you want.
	})
	    /***必修***/
	$("#obligatory-span").click(function(){
	    // 當點到圖案時，若內容是隱藏時則顯示它；反之則隱藏
	    $('#obligatory-post').slideToggle();
	    $('#obligatory-span').find("span").toggle();
	});                
	    /***選修***/
	$("#elective-span").click(function(){
	    $('#elective-post').slideToggle();
	    $('#elective-span').find("span").toggle();
	});
	    /***通識***/
	$("#general-span").click(function(){
	    $('#general-post').slideToggle();
	    $('#general-span').find("span").toggle();
	});
	    /***體育***/
	$("#school-span").click(function(){
	    $('#school-post').slideToggle();
	    $('#school-span').find("span").toggle();

	});
	    /***搜尋***/
	$("#search-span").click(function(){
	    $('#search-post').slideToggle();
	    $('#search-span').find("span").toggle();
	});
	    /***一年級***/
	$("#freshman-head").click(function(){
	    $("#freshman-head").find("span").toggle();
	    $("#freshman").find("button").toggle("slow");
	});

	$("#sophomore-head").click(function(){
	    $("#sophomore-head").find("span").toggle();
	    $("#sophomore").find("button").toggle("slow");
	});
	$("#junior-head").click(function(){
	    $("#junior-head").find("span").toggle();
	    $("#junior").find("button").toggle("slow");
	});
	$("#senior-head").click(function(){
	    $("#senior-head").find("span").toggle();
	    $("#senior").find("button").toggle("slow");
	});
	$("#fifth-grade-head").click(function(){
	    $("#fifth-grade-head").find("span").toggle();
	    $("#fifth-grade").find("button").toggle("slow");
	});
	$("#whole-school-head").click(function(){
	    $("#whole-school-head").find("span").toggle();
	    $("#whole-school").find("button").toggle("slow");
	});


	/*******   ↑製作隱藏側欄的功能↑   *******/
	
	/*******       ↓雙主修選擇↓       *******/
	$("#checkbox").click(function(){
	    if($(this).val() == "noDoubleMajor"){
	        $(this).val("DoubleMajor");
	        $('#degree_div').toggle("slow");
	        $('#major_div').toggle("slow");
	        $('#level_div').toggle("slow");                        
	        $("#d_major_group").toggle("slow");
	        $("#d_level_group").toggle("slow");
	        $("#textForDM").toggle("slow");
	    }
	    else{
	        $(this).val("noDoubleMajor");
	        $('#degree_div').toggle("slow");
	        $('#major_div').toggle("slow");
	        $('#level_div').toggle("slow");    
	        $("#d_major_group").toggle("slow");
	        $("#d_level_group").toggle("slow");
	        $("#textForDM").toggle("slow");
	    }
	});
	$('#storecheck').click(function(){
		if($(this).val()=='post'){
			$(this).val('get');
			$('#postform').toggle('slow');
			$('#alotbutton').toggle('slow');
			$('#footer_btn').toggle('slow');
			$('#get_form').toggle('slow');
		}
		else{
			$(this).val('post');
			$('#postform').toggle('slow');
			$('#alotbutton').toggle('slow');
			$('#footer_btn').toggle('slow');
			$('#get_form').toggle('slow');

		}
	})
	/*******       ↑雙主修選擇↑       *******/

	$("#bulletin").delegate("span.fa-trash", "click", function(){//這是給垃圾桶用的
	    if($(this).parents("button").attr("class")=="close elective"){
	        $("#freshman").empty();
	        $("#sophomore").empty();
	        $("#junior").empty();
	        $("#senior").empty();
	        $("#fifth-grade").empty();
	    }
	    else if($(this).parents("button").attr("class")=="close general"){
	        $('#humanities').empty();
	        $('#social').empty();
	        $('#natural').empty();
	    }
	    else if($(this).parents("button").attr("class")=="close school"){
	        $('#chinese').empty();
	        $('#english').empty();
	        $('#PE-post').empty();
	        $('#military-post').empty();
	        $('#teacher-post').empty();
	        $('#foreign-post').empty();
	        $('#non-graded-optional-post').empty();
	    }
	    else{
	        $(this).parents(".panel-heading").next().empty();
	    }
	});
	/**********用來把夜校的欄位隱藏起來***********/
	$("#toggleTable").click(function(){             
	    if($("#toggleTable").val()=="moon")
	    {
	        $("tr:gt(0)").toggle("slow");
	        $("tr:gt(9)").toggle("slow");
	        $(this).val("all");
	        $("#sun-span").toggle("slow");
	    }
	    else if($("#toggleTable").val()=="all"){
	        $("tr:gt(9)").toggle("slow");
	        $(this).val("sun");
	        $("#moon-span").toggle("slow");
	    }
	    else
	    {
	        $("tr:gt(0)").toggle("slow");
	        $(this).val("moon");
	        $(this).find("span").toggle("slow");
	    }
	});
	
	$("#booklistbtn").click();
	/*****************************************************************************
	Becuase the "booklist field" was hiddened by default.
	When the html page is loaded, automatically clicked it, no matter it already have book list or not.
  If it didn't hava any booklist, the field will be empty and show nothing, which didn't occupy any space; if it already have booklist, just show it.
	*****************************************************************************/
});
var group_of_reset = function(){
    $(".search_result").empty();//以下是要清掉選修課程、指定時間搜尋等課程
    // $('#freshman').empty();
    // $('#sophomore').empty();
    // $('#senior').empty();
    // $('#junior').empty();
    // $('#fifth-grade').empty();
    // $('#sixth-grade').empty();
    // $('#seventh-grade').empty();
    // $('#whole-school').empty();
    // $('#humanities').empty();
    // $('#social').empty();
    // $('#natural').empty();
    // $('#chinese').empty();
    // $('#english').empty();
    // $('#PE-post').empty();
    // $('#military-post').empty();
    // $('#teacher-post').empty();
    // $('#foreign-post').empty();
    // $('#non-graded-optional-post').empty();
}
/***********清除***********/
var reset=function(){
    $('#time-table td').empty(); //把目前的time-table清空，好讓下個年級的課程能夠乾淨的顯示
    $("td").html('<span class="fa fa-plus-circle fa-5x"></span>');  //再把加號的按鈕填上去
    group_of_reset();
    $(".search_result").empty();
    window.credits=0;
    $("#class_credit").text(window.credits);
    window.name_of_optional_obligatory=[];  //把數過的課程清空                
    window.user=return_init_user_json();
}
/********用+字號功能時，清空側欄********/
var reset_for_time_request=function(){  //這個function是在你的td的時候，會把該時段的課程顯示，但是要先把顯示欄位清空
    group_of_reset();
}
/*側邊欄toggle*/

$("#booklistbtn").click(function(){
	  $('#booklist').toggle("slow");
});
