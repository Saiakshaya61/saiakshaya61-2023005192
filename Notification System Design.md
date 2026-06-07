Notification System Design

Priority Calculation

Placement = 3

Result = 2

Event = 1

Notifications are sorted based on:

1. Priority Weight
2. Timestamp (Most Recent First)

Top 10 Notifications

After sorting all notifications, the first 10 notifications are displayed as the Priority Inbox.

Efficient Maintenance

To efficiently maintain the Top 10 notifications when new notifications arrive:

- Use a Min Heap of size 10.
- Insert each notification based on its priority.
- If the heap size exceeds 10, remove the lowest-priority notification.

Time Complexity: O(log 10)