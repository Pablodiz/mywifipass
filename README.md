# MyWifiPass

**MyWifiPass** is a comprehensive tool environment designed to simplify and streamline the implementation of EAP-TLS authentication methods in enterprise wireless networks.

## Overview

In today's environments, securing wireless networks with robust authentication mechanisms is crucial. EAP-TLS (Extensible Authentication Protocol - Transport Layer Security) provides one of the most secure authentication methods available, using digital certificates for both client and server authentication. However, implementing and managing EAP-TLS can be complex and time-consuming.

MyWifiPass addresses these challenges by providing an integrated solution that combines:
- **Certificate Management**: Automated generation of digital certificates for Wi-Fi clients and networks.
- **RADIUS Server Integration**: Automated configuration of a FreeRADIUS server, providing the configurations of every managed network.
- **User-Friendly Interface**: Intuitive web-based dashboard for managing Wi-Fi clients and networks.
- **Android App**: Automated configuration of networks in an Android app. 
- **Network Management**: Integrations with OpenWISP for centralized access point configuration and monitoring.

## The Wi-Fi Pass Concept

MyWifiPass was designed around the scenario of event venues where secure networks must be deployed frequently. In these environments, users store their credentials as **"Wi-Fi passes"** - similar to event tickets, but containing digital certificates for network authentication.

These Wi-Fi passes can be easily shared via QR codes and automatically configure user devices with all necessary certificates and network settings. This approach makes enterprise-grade wireless security accessible for temporary deployments while maintaining high security standards for events with strict requirements like voting or competitions.

## Parts 

At the moment, MyWifiPass is formed of two main tools:

### MyWifiPass System
**Repository**: [mywifipass_system](https://github.com/Pablodiz/mywifipass_system)


A comprehensive web application for managing Wi-Fi clients and networks. Key features include:
- **User Management**: Create and manage Wi-Fi users with automatic certificate generation
- **Network Configuration**: Define and configure multiple wireless networks 
- **RADIUS Integration**: Automatically configures FreeRADIUS server with EAP-TLS settings
- **Certificate Management**: Full PKI lifecycle including generation, distribution and revocation
- **Email Notifications**: Automated certificate delivery
- **API Access**: RESTful API for integration with third-party systems
- **OpenWISP Integration**: Simplified setup and basic configuration of OpenWISP for access point management


### MyWifiPass Android
**Repository**: [mywifipass_android](https://github.com/Pablodiz/mywifipass_android)

An Android application that simplifies the complex process of configuring EAP-TLS networks on mobile devices:
- **QR Code Scanning**: Instant Wi-Fi Pass download QR codes generated by the web system
- **Certificate Installation**: Automated installation of client certificates and CA certificates
- **Network Profiles**: Save and manage multiple network configurations
- **User-Friendly Interface**: Intuitive design requiring no technical knowledge

## Use Cases

MyWifiPass aims to help organizations of all sizes implement enterprise-grade wireless security without the complexity and cost traditionally associated with EAP-TLS deployments. Some key use cases include:

- **Events & Conferences**: Temporary secure networks with easy attendee onboarding
- **Hotels & Hospitality**: Secure guest Wi-Fi with individual authentication  
- **Small to Medium Businesses**: Enterprise-grade security without the enterprise complexity
- **Educational Institutions**: Student and faculty wireless authentication

