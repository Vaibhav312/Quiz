window.onload = sendApiRequest


async function sendApiRequest() {
    let response = await fetch("https://opentdb.com/api.php?amount=10&type=multiple");

    let data = await response.json();
    // console.log(data);
    useApirequest(data);

}

$(function() {
    $('.navbar-collapse a').click(function() {

        $(".navbar-collapse ").collapse('hide');
    });

});

$(window).on('load', function() {
    if ($('.cover').length) {
        $('.cover').parallax({
            imageSrc: $('.cover').data('image'),
            zIndex: '1'
        });
    }

    $("#preloader").animate({
        'opacity': '0'
    }, 600, function() {
        setTimeout(function() {
            $("#preloader").css("visibility", "hidden").fadeOut();
        }, 300);
    });
});



function useApirequest(data) {

    $category_value = data.results[0].category;
    $difficulty_value = data.results[0].difficulty;
    $question_value = data.results[0].question;
    $category_value = data.results[0].category;
    $correct_answer = data.results[0].correct_answer;
    $wrong_value1 = data.results[0].incorrect_answers[0];
    $wrong_value2 = data.results[0].incorrect_answers[1];
    $wrong_value3 = data.results[0].incorrect_answers[2];


    $("#category").html("Category: " + $category_value);
    $("#difficulty").html("Difficulty: " + $difficulty_value);
    $("#question").html("Question: " + $question_value);
    //$("#category").html($category_value);
    $("#answer1").html($correct_answer);
    $("#answer2").html($wrong_value1);
    $("#answer3").html($wrong_value2);
    $("#answer4").html($wrong_value3);
}

$(document).ready(function() {
    var count = 1;
    var progess = 0;

    var sum = 0;

    setInterval(updateCountdown, 1000);

    (function($) {



        $(".answer_buttons").click(function() {
            $("#correct_answer_ques").html("Previous Question: " + $question_value + "<br/>");
            $("#correct_answer_display").html("Correct Answer: " + $correct_answer);
            //  $("#correct_answer_display").html(" Previous Question:  "+  $question_value+"</br>Correct Answer: "+$correct_answer);
            if (count <= 10) {

                sendApiRequest();
                shuffleElements($('.answer_buttons'));
                count++;


            }
        });
        if (count == 10) {
            $("#correct_answer_ques").html(" Previous Question:  " + $question_value + "<br/>");
            $("#correct_answer_display").html("Correct Answer: " + $correct_answer);
        }

    })(jQuery);

    $('.answer_buttons').click(function() {

        progess = progess + 10;
        $(".progress-bar").css("width", progess + '%').attr('aria-valuenow', progess);
        $("#progres_bar_value").html((progess / 10) <= 10 ? progess + " %" : 100 + " %");

        var fired_button = $(this).attr('id');
        var correct_button = $("#answer1").attr('id');
        if (fired_button == correct_button) {
            sum = sum + 10;
        }
        $("#result_score_display").html("Total Score:" + sum + "/ 100 ");
    });








    /****************************************************** Timer ************************************************/


    const startingMinutes = 03;
    var time = startingMinutes * 60;


    function updateCountdown() {

        const minute = Math.floor(time / 60);
        let seconds = time % 60;
        seconds = seconds < 10 ? '0' + seconds : seconds;
        document.getElementById('timer').innerHTML = minute + ":" + seconds;
        console.log(minute);
        console.log(seconds);
        time--;
        if (minute == 0 && seconds == 0) {
            //alert("Time's up");
            document.location.href = $("#Url").attr("data-url");
        }


    }

    /******************************************************************************shuffle indexes*****************************************************************/
    function shuffleElements($elements) {
        var i, index1, index2, temp_val;

        var count = $elements.length;
        var $parent = $elements.parent();
        var shuffled_array = [];


        for (i = 0; i < count; i++) {
            shuffled_array.push(i);
        }
        for (i = 0; i < count; i++) {
            index1 = (Math.random() * count) | 0;
            index2 = (Math.random() * count) | 0;

            temp_val = shuffled_array[index1];
            shuffled_array[index1] = shuffled_array[index2];
            shuffled_array[index2] = temp_val;
        }

        // apply random order to elements
        $elements.detach();
        for (i = 0; i < count; i++) {
            $parent.append($elements.eq(shuffled_array[i]));
        }
    }


});