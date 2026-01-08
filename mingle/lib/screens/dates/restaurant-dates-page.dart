import 'package:flutter/material.dart';
import 'package:mingle/screens/dates/restaurant-dates-card.dart';

class RestaurantDatePage extends StatelessWidget {
  RestaurantDatePage({super.key});

  // To replace with getDatesArray or sth
  // May need to get name & photo from user's ID separately
  final List<Map<String, dynamic>> matches = [
    {
      "a": {
        "id": "user_001",
        "name": "Alex",
        "photo": "https://randomuser.me/api/portraits/men/32.jpg",
      },
      "b": {
        "id": "user_002",
        "name": "Jamie",
        "photo": "https://randomuser.me/api/portraits/women/44.jpg",
      },
      "dateTime": "2026-01-07T18:30:00",
      "matchId": "match_001",
    },
     {
      "a": {
        "id": "user_003",
        "name": "Charlie",
        "photo": "https://randomuser.me/api/portraits/men/32.jpg",
      },
      "b": {
        "id": "user_004",
        "name": "Dawn",
        "photo": "https://randomuser.me/api/portraits/women/44.jpg",
      },
      "dateTime": "2026-01-07T18:30:00",
      "matchId": "match_001",
    },
     {
      "a": {
        "id": "user_005",
        "name": "Ele",
        "photo": "https://randomuser.me/api/portraits/men/32.jpg",
      },
      "b": {
        "id": "user_006",
        "name": "Faith",
        "photo": "https://randomuser.me/api/portraits/women/44.jpg",
      },
      "dateTime": "2026-01-07T18:30:00",
      "matchId": "match_001",
    },
  ];

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: matches.length,
      itemBuilder: (context, index) {
        return RestaurantDateCard(match: matches[index]);
      },
    );
  }
}
