## API

- Application Programming Interface
- A contract that defines between client and server
  - What requests can be made
  - How to make them
  - What response to expect

- Abstraction Mechanism
- Service Boundaries

###

    - REST
      - Resource based - Organised around resources using HTTP methods
      - Stateless - Each req contains all info needed
      - Standard methods: GET, POST, PUT, PATCH, DELETE
      - Most common API style
      - Web & Mobile Apps

    - GraphQL
      - Query Lang - Clients re exactly what they need
      - Single Endpoint - 1 endpoint for all operations
      - Operations - Query(read), Mutation(write), Subscription(real-time)
      - Minimal round trips
      - Complex UIs

    - gRPC
      - Protocol Buffers - Binary serializtion with scema definitions
      - Service definition - Methods defined as RPCs in .proto files
      - Communication Types - Unary, Srver streaming, Client Streaming, Bidirectional Streaming
      - High Performance
      - Microservices

## Key Design Priciples

Consistency
Consisten Naming
Consistent Patterns

Simplicicty
Focus on core use cases
intuative design

Security
Autrhentication
Authorization
Input Validation
rate Limiting

Performance
Caching strategies
pagination
Minimize payloads
Reduce round trips

## Protocols

HTTP - RESTful APIs
Status Codes - CRUD operations
Websockets - Real time APIs
gRPC -
AMQP

## Design Approaches

Top - Down : High level requirements to workflows
Bottom up - begin with existing data models and capabilities
Contract first - define api contract before implementation

## API lifecycle management

design
development
deployment & monitoring
maintainence
deprecation & retirement

## SECURITY

- Rate limiting
- CORS
- SQL & NO SQL Injection
- Firewalls
- VPN
- CSRF
- XSS
-
