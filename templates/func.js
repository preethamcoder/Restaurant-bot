var count = 0;
          function getBotResponse() {
            var rawText = $("#nameInput").val();
            var userHtml =
              '<p class="userText"><span><b>' +
              "You : " +
              "</b>" +
              rawText +
              "</span></p>";
            $("#nameInput").val("");
            $("#chatbox").append(userHtml);
            document
              .getElementById("userInput")
              .scrollIntoView({ block: "start", behavior: "smooth" });
            $.get("/get", { msg: rawText }).done(function (data) {
              var botHtml =
                '<p class="botText"><span><b>' +
                "Saanya : " +
                "</b>" +
                data +
                "</span></p>";
              $("#chatbox").append(botHtml);
              document
                .getElementById("userInput")
                .scrollIntoView({ block: "start", behavior: "smooth" });
            });
          }
          $("#nameInput").keypress( function (e) {
            if (e.which == 13) {

          

              // $("#chatbox").animate({
              //   scrollTop: 100
              // },750)
               getBotResponse();


            setTimeout(() => {
              document.getElementById("chatbox").scrollTo({top : document.getElementById("chatbox").scrollHeight,behavior:'smooth'})
            
            },500)
            //  document.getElementById("chatbox").scrollTo({top : document.getElementById("chatbox").scrollHeight,behavior:'smooth'})
            }
          });

          $(".button-1").click(() => {
            getBotResponse();
            setTimeout(() => {
              document.getElementById("chatbox").scrollTo({top : document.getElementById("chatbox").scrollHeight,behavior:'smooth'})
            
            },500)
          });
