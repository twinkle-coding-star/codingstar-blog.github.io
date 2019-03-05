생명주기에 따라,  net.Server가 발생시키는 이벤트

listening

IP 주소와, Port를 listening 할 때

connection

새로운 connection이 체결되었을 때, 콜백함수는 socket 객체를 전달 받게 된다.

close

서버가 closed일 때, port에 바인딩 해제 된다.

error

서버 레벨에서 에러가 발생했을 때, 