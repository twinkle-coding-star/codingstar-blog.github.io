Firebase

클라우드 서비스 + 프로그래밍 인터페이스 + 라이브러리

서비스를 관리하는 웹 기반 콘솔과 결합 = 서버와 서비스를 Firebase에서 제공



클라우드 메시징(Cloud Messaging)



알림을 전달 할 때 데이터까지 전달하기

```swift
Bundle customData = getIntent().getExtras();
        if(customData != null) {
            String notiMsg = customData.getString("MyKey");
            Log.d(TAG, notiMsg);
        }
```

알림을 눌렀을 때, 실행되는 액티비티로 데이터를 포함한 인텐트가 넘어온다.

해당 액티비티에서, Firebase에서 설정한 Key를 통해 값을 가져올 수 있다.



포그라운드에서 알림 받기

FirebaseMessagingService 클래스의 onMessageReceived를 오버라이딩한 클래스를 만든다.

```java
public class MyFBMessageService extends FirebaseMessagingService {
    public final static String TAG = MyFBMessageService.class.getName();

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);
        Log.d(TAG, "Title : " + remoteMessage.getNotification().getTitle());
        Log.d(TAG, "Message : " + remoteMessage.getNotification().getBody());
    }

}
```

onMessageReceived 메서드의 RemoteMessage 객체를 통해, 전달받은 알림을 확인할 수 있다.





서비스 클래스를 AndroidManifest.xml에 등록한다.

```xml
<service android:name=".MyFBMessageService"
    android:enabled="true"
    android:exported="true">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT"/>
    </intent-filter>
</service>
```