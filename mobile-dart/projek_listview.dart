import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:readmore/readmore.dart';

void main() {
  runApp(Aplikasi());
}

class Aplikasi extends StatelessWidget {
  List<Container> myList = [
    Container(
      height: 300,
      width: 400,
    ),
    Container(
      height: 300,
      width: 400,
      color: Colors.amber,
    ),
    Container(
      height: 300,
      width: 400,
      color: Colors.green,
    ),
    Container(
      height: 300,
      width: 400,
      color: Colors.red,
    ),
    Container(
      height: 300,
      width: 400,
      color: Colors.purple,
    ),
  ];

  List<Color> myColor = [
    Colors.red,
    Colors.amber,
    Colors.pink,
    Colors.purple,
    Colors.orange,
  ];

  List<AssetImage> myImage = [
    AssetImage("images/burger.jpg"),
    AssetImage("images/cake.jpg"),
    AssetImage("images/kebab.jpg"),
    AssetImage("images/kurma.jpg"),
    AssetImage("images/madu.jpg"),
  ];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text("Listview"),
      ),
      body: ListView.separated(
        separatorBuilder: (context, index) {
          return Container(
            height: 100,
            width: 100,
            child: Column(
              children: [
                Container(
                  height: 20,
                  child: Row(
                    children: [
                      new IconButton(
                        alignment: Alignment.centerLeft,
                        onPressed: () {},
                        icon: new Icon(Icons.favorite_border_rounded),
                      ),
                      new IconButton(
                        alignment: Alignment.centerRight,
                        onPressed: () {},
                        icon: new Icon(Icons.comment_rounded),
                      ),
                      new IconButton(
                        alignment: Alignment.centerLeft,
                        onPressed: () {},
                        icon: Icon(Icons.share_rounded),
                      ),
                    ],
                  ),
                ),
                SingleChildScrollView(
                    child: Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: ReadMoreText(
                    "selamat datang aplikasi, halo semua saya sedang belajar flutter dan masih pemula " +
                        "selamat belajar " +
                        "saya sangat senang walaupun pusing",
                    textAlign: TextAlign.justify,
                    trimLines: 2,
                    trimMode: TrimMode.Line,
                    trimCollapsedText: "More",
                    trimExpandedText: "Less",
                    style: TextStyle(
                        color: Colors.red,
                        fontWeight: FontWeight.bold,
                        fontSize: 20,
                        letterSpacing: 2,
                        fontFamily: 'Roboto'),
                  ),
                )),
              ],
            ),
          );
        },
        itemCount: myColor.length,
        itemBuilder: (context, index) {
          return Container(
            height: 300,
            width: 400,
            color: myColor[index],
            child: Image(
              fit: BoxFit.cover,
              image: myImage[index],
            ),
          );
        },
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.people), label: 'Profile'),
          BottomNavigationBarItem(icon: Icon(Icons.chat), label: 'Message'),
          BottomNavigationBarItem(icon: Icon(Icons.settings), label: 'Setting'),
        ],
        currentIndex: 0,
        selectedItemColor: Colors.blue,
        unselectedItemColor: Colors.grey,
      ),
    ));
  }
}
