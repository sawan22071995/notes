# How to start openvidu local setup

1. Start the openvidu server

```bash
$ docker run -p 4443:4443 --rm -e OPENVIDU_SECRET=MY_SECRET openvidu/openvidu-server-kms:2.14.0
```

2. Start the backend

```bash
$ cd /home/manohar/projects/personal/learning/openvidu_related/openvidu_call/openvidu-call
$ npm run start --prefix openvidu-call-back
```

3. Start the frontend

```bash
$ cd /home/manohar/projects/personal/learning/openvidu_related/openvidu_call/openvidu-call/openvidu-call-front
$ npx ng serve --open
```

4. URLs

<https://localhost:4443/dashboard/#/> - dashboard to test

<https://localhost:4443/> - Rest APIs URL

<http://localhost:4200/#/> - App URL