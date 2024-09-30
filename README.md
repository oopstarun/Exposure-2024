# Exposure-2024
# Event Registration Tracker

## Overview

The **Event Registration Tracker** is a web-based application designed to streamline the process of creating, managing, and tracking event registrations. It provides an intuitive platform for event organisers and attendees, allowing for easy RSVP and efficient organisation of event details.

## Table of Contents

1. [Introduction](#introduction)
2. [Overall Description](#overall-description)
3. [Functional Requirements](#functional-requirements)
4. [Testing Requirements](#testing-requirements)
5. [Creative Features and Suggestions](#creative-features-and-suggestions)
6. [Use Cases](#use-cases)
7. [Conclusion](#conclusion)
8. [Datasets](#datasets)

## Introduction

### Purpose

The Event Registration Tracker aims to provide a user-friendly platform for event organisers to create and manage events, while also allowing users to easily register and provide feedback.

### Scope

The application will enable event organisers to:
- Create and manage events.
- Allow users to register and RSVP.
- Track attendees and send notifications.
- Provide a platform for user feedback and reviews.

### Audience

The intended audience includes event organisers, attendees, and administrators who manage event registrations and feedback.

## Overall Description

### Product Perspective

The application is accessible via modern web browsers and features user-friendly interfaces for both organisers and attendees.

### Product Functions

- **Event Management**: Create, update, and delete events.
- **Registration Management**: Allow users to register for events, update their registration, and cancel if necessary.
- **Attendee Tracking**: Monitor attendee lists and send reminders.
- **Feedback System**: Collect and display user reviews and ratings for events.

## Functional Requirements

- **User Registration and Login**
  - Users can create an account using an email address and password.
  - Users can log in and log out of their accounts.
  
- **Event Management**
  - Organisers can create, update, and delete events.
  - Events should be categorised (e.g., workshops, seminars, social gatherings).
  
- **Registration and RSVP**
  - Users can view upcoming events and register.
  - Users can update or cancel their registrations.

- **Attendee Tracking**
  - Organisers can view registered attendees and receive confirmation and reminder emails.

- **Feedback System**
  - Users can submit feedback and ratings for events.

## Testing Requirements

### Testing Strategy

Testing will include unit testing, integration testing, and user acceptance testing to ensure all functional requirements are met.

### Test Cases

| Test Case ID | Description                     | Input                           | Expected Output                     |
|--------------|---------------------------------|---------------------------------|-------------------------------------|
| TC1          | Test user registration          | Valid email and password        | User account created successfully    |
| TC2          | Test user login                 | Valid email and password        | User logged in successfully          |
| TC3          | Test event creation             | Event details                   | Event created successfully           |
| TC4          | Test event update               | Updated event details           | Event updated successfully           |
| TC5          | Test event deletion             | Event ID                       | Event deleted successfully           |
| ...          | ...                             | ...                             | ...                                 |

## Creative Features and Suggestions

- **Event Reminder System**: Personalised reminders based on user preferences.
- **QR Code for Registration**: Unique QR codes for easy check-in at events.
- **Social Media Integration**: Share registrations on social media for increased visibility.
- **Custom Event Themes**: Organisers can choose themes for their events.
- **Gamification**: Points system for user engagement and discounts.

## Use Cases

| Use Case ID | Use Case Name          | Description                       |
|--------------|------------------------|-----------------------------------|
| UC1          | User Registration      | A user registers for an account.  |
| UC2          | Event Creation         | An organiser creates a new event. |
| UC3          | Event Registration     | A user registers for an event.    |
| UC4          | Feedback Submission    | A user submits feedback for an event. |

## Conclusion

The Event Registration Tracker aims to enhance the experience of event management for both organisers and attendees by providing a comprehensive tool that streamlines the registration process.

## Datasets

1. **Participants Dataset**: Stores information about participants and their preferences.
2. **Events Dataset**: Contains information about organised events.
3. **Registrations Dataset**: Tracks participant registrations for events.
4. **Feedback Dataset**: Stores feedback from participants after events.

## File Formats

- **CSV Files**: For Participants, Events, Registrations, and Feedback data.
- **JSON Files**: For Participants, Events, Registrations, and Feedback data.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to this project!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
