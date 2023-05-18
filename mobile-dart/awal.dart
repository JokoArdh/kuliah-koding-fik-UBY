import 'package:flutter/material.dart';

void main() {
  runApp(selamat());
}

class selamat extends StatelessWidget {
  const selamat({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Color.fromARGB(255, 127, 216, 86),
        body: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            children: [
              SizedBox(height: 30),
              CircleAvatar(
                backgroundImage: AssetImage('images/lgt.jpg'),
                radius: 80,
              ),
              Text(
                'Selamat Datang Kembali',
                style: TextStyle(
                    fontFamily: 'Nunito',
                    fontSize: 28,
                    color: Colors.white,
                    fontWeight: FontWeight.w600),
              ),
              Text(
                'Silahkan Login',
                style: TextStyle(
                    fontFamily: 'Nunito',
                    fontSize: 24,
                    color: Color.fromARGB(255, 141, 126, 126),
                    fontWeight: FontWeight.w600),
              ),
              SizedBox(
                height: 51,
              ),
              Row(
                children: [
                  Expanded(
                    child: Container(
                      height: 46,
                      decoration: BoxDecoration(
                        color: Colors.blueAccent,
                        borderRadius: BorderRadius.circular(13),
                      ),
                      child: Center(
                        child: Text(
                          "Login",
                          style: TextStyle(
                              fontSize: 20,
                              fontFamily: "Nunito",
                              color: Colors.white,
                              fontWeight: FontWeight.w700),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
              SizedBox(
                height: 10,
              ),
              Row(
                children: [
                  Expanded(
                    child: Container(
                      height: 1,
                      color: Colors.white,
                    ),
                  ),
                  SizedBox(width: 10),
                  Text(
                    "atau",
                    style: TextStyle(
                        fontSize: 20,
                        fontFamily: "Nunito",
                        fontWeight: FontWeight.w700,
                        color: Colors.white),
                  ),
                  SizedBox(
                    width: 10,
                  ),
                  Expanded(
                    child: Container(
                      height: 1,
                      color: Colors.white,
                    ),
                  )
                ],
              ),
              SizedBox(
                height: 10,
              ),
              Row(
                children: [
                  Expanded(
                    child: Container(
                      height: 46,
                      decoration: BoxDecoration(
                        color: Colors.blueAccent,
                        borderRadius: BorderRadius.circular(13),
                      ),
                      child: Center(
                        child: Text(
                          "Sign Up",
                          style: TextStyle(
                            fontFamily: 'Nunito',
                            fontWeight: FontWeight.w700,
                            color: Colors.white,
                            fontSize: 20,
                          ),
                        ),
                      ),
                    ),
                  )
                ],
              ),
              Expanded(child: SizedBox()),
              Text(
                "@2023 Himatek Production",
                style: TextStyle(
                  fontSize: 15,
                  fontFamily: 'Nunito',
                  color: Color.fromARGB(255, 54, 47, 47),
                  fontWeight: FontWeight.w700,
                ),
              ),
              SizedBox(
                height: 24,
              )
            ],
          ),
        ),
      ),
    );
  }
}
