import 'package:flutter/material.dart';

void main() => runApp(const AutoAttendanceApp());

class AutoAttendanceApp extends StatelessWidget {
  const AutoAttendanceApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AutoAttendance',
      themeMode: ThemeMode.system,
      theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo, brightness: Brightness.light),
      darkTheme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo, brightness: Brightness.dark),
      home: const DashboardScreen(),
    );
  }
}

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final cards = [
      ('Quick Attendance', Icons.video_camera_back, 'Record a 5-10 second classroom panorama.'),
      ('Reports', Icons.analytics, 'Daily, weekly, monthly, and semester exports.'),
      ('Students', Icons.groups, 'Enroll students and capture face poses.'),
      ('Alerts', Icons.notifications_active, 'Low attendance and save confirmations.'),
    ];
    return Scaffold(
      appBar: AppBar(title: const Text('AutoAttendance')),
      body: GridView.builder(
        padding: const EdgeInsets.all(16),
        gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(maxCrossAxisExtent: 360, childAspectRatio: 1.25, mainAxisSpacing: 16, crossAxisSpacing: 16),
        itemCount: cards.length,
        itemBuilder: (context, index) {
          final card = cards[index];
          return Card(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Icon(card.$2, size: 36),
                const Spacer(),
                Text(card.$1, style: Theme.of(context).textTheme.titleLarge),
                const SizedBox(height: 8),
                Text(card.$3),
              ]),
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton.extended(onPressed: () {}, icon: const Icon(Icons.play_arrow), label: const Text('Start Attendance')),
    );
  }
}
