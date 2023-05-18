import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';

void main() {
  runApp(uts());
}

class uts extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Widget imageSection = Container(
    //   child: Image.asset(
    //     'images/madu.jpg',
    //     height: 250,
    //     width: 280,
    //     fit: BoxFit.cover,
    //   ),
    // );

    Widget textSection = Container(
      padding: EdgeInsets.only(top: 16, bottom: 20),
      child: Text(
        "dan hati hati saat melangkah    selalu perhatik",
        style: TextStyle(
            color: Colors.red, fontWeight: FontWeight.bold, fontSize: 18),
        textAlign: TextAlign.center,
      ),
    );

    Widget buttonSection = Container(
      width: 100,
      height: 45,
      padding: EdgeInsets.only(top: 9),
      child: TextButton(
        style: TextButton.styleFrom(
          backgroundColor: Colors.red,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
          ),
        ),
        onPressed: () {},
        child: Text(
          "Informasi Jalur Commuter",
          style: TextStyle(
            color: Colors.white,
          ),
        ),
      ),
    );

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            "KRL ACCESS",
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
            ),
          ),
          backgroundColor: Colors.red,
          leading: Icon(Icons.menu),
        ),
        body: ListView(
          children: [
            CarouselSlider(
              items: [
                Container(
                  margin: EdgeInsets.all(8.0),
                  decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10.0),
                      image: DecorationImage(
                          image: AssetImage('images/madu.jpg'),
                          fit: BoxFit.cover)),
                ),
                Container(
                  margin: EdgeInsets.all(8.0),
                  decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10.0),
                      image: DecorationImage(
                          image: AssetImage('images/madu.jpg'),
                          fit: BoxFit.cover)),
                ),
                Container(
                  margin: EdgeInsets.all(8.0),
                  decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10.0),
                      image: DecorationImage(
                          image: AssetImage('images/madu.jpg'),
                          fit: BoxFit.cover)),
                ),
              ],
              options: CarouselOptions(
                  height: 250.0,
                  enlargeCenterPage: true,
                  autoPlay: true,
                  aspectRatio: 16 / 9,
                  autoPlayCurve: Curves.fastOutSlowIn,
                  enableInfiniteScroll: true,
                  autoPlayAnimationDuration: Duration(milliseconds: 800),
                  viewportFraction: 0.8),
            ),
            textSection,
            buttonSection,
            SingleChildScrollView(
              scrollDirection: Axis.vertical,
              child: Column(
                children: [
                  ListTile(
                    title: Text(
                      "CIKARANG LINE",
                      style: TextStyle(
                          fontWeight: FontWeight.bold, color: Colors.blue),
                    ),
                    subtitle:
                        Text("KA 5076B (Ak-Bks Terakhir) menuju transit.."),
                  ),
                  ListTile(
                    title: Text(
                      "BOGOR LINE",
                      style: TextStyle(
                          fontWeight: FontWeight.bold, color: Colors.red),
                    ),
                    subtitle:
                        Text("KA 4450 (jakk-boo Terakhir) menuju transit.."),
                  ),
                  ListTile(
                    title: Text(
                      "TANJUNGPRIUK LINE",
                      style: TextStyle(
                          fontWeight: FontWeight.bold, color: Colors.purple),
                    ),
                    subtitle: Text("Perjalanan Normal"),
                  ),
                  ListTile(
                    title: Text(
                      "RANGKASITUNG LINE",
                      style: TextStyle(
                          fontWeight: FontWeight.bold, color: Colors.green),
                    ),
                    subtitle:
                        Text("KA 2176 (Thb-Prp Terakhir) menuju transit.."),
                  ),
                  ListTile(
                    title: Text(
                      "TANGERANG LINE",
                      style: TextStyle(
                          fontWeight: FontWeight.bold, color: Colors.yellow),
                    ),
                    subtitle:
                        Text("KA 2366 (Du-Too Terakhir) menuju transit.."),
                  )
                ],
              ),
            ),
          ],
        ),
        floatingActionButton: FloatingActionButton(
          child: Icon(Icons.undo),
          onPressed: () {},
          backgroundColor: Colors.red,
        ),
        bottomNavigationBar: BottomAppBar(
          child: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Container(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    "joko ardiyanto @ UTS_MOBILE tahun 2023",
                    style: TextStyle(color: Colors.white),
                  ),
                ],
              ),
            ),
          ),
          color: Colors.red,
        ),
      ),
    );
  }
}
