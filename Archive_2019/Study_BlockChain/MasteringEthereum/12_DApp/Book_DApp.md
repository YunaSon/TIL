# Decentralized Application - DApp (댑)
---------------------------------------------------------------------------------------------------------------

## 0. Introduction
#### 1) Decentralized Application - DApp은 웹을 재 발명하고, web3라고 불리는 댑의 새로운 세계를 만든다는 vision을 가지고 있다. 
#### 2) web3 댑은 스토리지(storage), 메시징(messiging), 네이밍(naiming)등 애플리케이션의 다른 모든 측면을 탈중앙화하는 것에 관한 것.
#### 3) 댑은 종종 웹프런트엔드 + 스마트 컨트랙트도 지칭하였으나 이것은 엄밀히 말하면 거짓이다. 
#### 4) 경매 플랫폼인 댑 샘플을 개발하고 배포하기. 

<img width="889" alt="web3" src="https://user-images.githubusercontent.com/39859458/69703509-e1a6d480-1134-11ea-9a22-ff81893bc389.png">



-----------------------------------------------------------------------------------------------------------------

##  1. 댑이란 무엇인가?
#### 즉, 탈중앙화된 애플리케이션, 탈중앙화가 가능한 측면은 무엇인가?
        - 백엔드(Backend) 소프트웨어
        - 프런트엔드(Frontend) 소프트웨어
        - 데이터 스토리지(Data Storage)
        - 메시지 통신(Message Communication)
        - 네임 레졸루션(name resolution)
#### (단일 측면에서) 탈중앙화 예시 ( != DApp은 아님)
        - 프런트엔드(Frontend) : 중앙 서버에서 실행되는 웹앱으로 개발, 개인의 단말기에서 실행되는 모바일 앱
        - 벡엔드(Backend),데이터 스토리지(Data Storage, DB)  : 사설 서버, 폐쇄적(proprietary)데이터 베이스, 스마트 컨트랙트, P2P스토리지. 
#### 장점
        - 지속성(resiliency)
        - 투명성(transparency)
        - 검열 저항(Censorship resistance)

   ### 1) 백엔드 (스마트 컨트랙트)
      - 일반적인 애플리케이션에서 서버측(백엔드)구성요소를 대체하는 것으로 스마트 컨트랙트를 생각해 볼 수 있다.
      - 댑에서 스마트 컨트랙트는 비지니스 로직(프로그램 코드)과 애플리케이션의 관련 상태를 저장하는데 사용된다. 
      - 서버 측 백엔드와 가장 큰 차이점 중 하나는 스마트 컨트랙트에서 실행되는 계산이 매우 비싸기 때문에 가능한 한 최소화해서 유지해야 한다는 것이다. 
      - 이더리움 스마트 컨트랙트를 이용하면, 스마트 컨트랙트 상호간 호출은 물론 데이터를 주고 받을 수 있으며, 자체의 상태 변수를 읽고 쓰는 네트워크 아키텍처를 만들 수 있다. 
      - 스마트 컨트랙트 아키텍처 설계의 고려사항1. 스마트 컨트랙트가 배포된 후 스마트 컨트랙트의 코드를 변경 할 수 없다.  
      - 스마트 컨트랙트 아키텍처 설계의 고려사항2. 댑의 크기. 
   ### 2) 프런트엔드 (웹 유저 인터페이스)
      - 댑의 클라이언트쪽 인터페이스는 표준 웹 기술(HTML, CSS, JS)를 사용한다. 
      - 메시지 서명, 트랜잭션 전송, 키관리 같은 이더리움과의 상호작용은 종종 메타마스크같은 확장 웹 브라우저에서 수행된다. 
      - web3.js 자바스크립트 라이브러리를 통해 이더리움에 연결된다. 
   ### 3) 데이터 스토리지
      - 높은 가스 비용과 현재의 낮은 블록 가스 한도 때문에 스마트 컨트랙트는 많은 양의 데이터를 저장하거나 처리하는데 적합하지 않다. 따라서 대부분의 댑은 오프체인 데이터 스토리지 서비스를 사용하는데 사이즈가 큰 데이터들을 이더리움 체인으로부터 데이터 스토리지 플랫폼으로 옮겨 저장한다. 
      - IPFS(Inter-Planetary File System): 저장된 객체를 P2P 네트워크 피어(peer)들에게 배포하는 탈중화된 콘텐츠 주소 부여 기능 스토리지 시스템.
      - 스웜: P2P시스템 
   ### 3) 탈중앙화 메시지 통신 프로토콜
      - 프로세스간 통신
      - 댑의 가장 주목할 만한 P2P메시징 프로토콜은 이더리움 재단의 고-이더리움 도구 모음의 일부인 위스퍼(Whisper, http://bit.ly/2CSls5h)

---------------------------------------------------------------------------------------------------------------


## 2. 기본 댑 사례: 경매 댑 
댑은 사용자가 주택, 자동차, 상표 같은 고유한 자산을 나타내는 증서(deed) 토큰을 등록할 수 있게 한다. 토큰이 등록되면 토큰 소유권이 경매 댑으로 이전되며, 판매를 위해 리스팅될 수 있게 해준다.
경매 댑은 등록된 각 토큰을 나열하여 다른 사용자가 입찰할 수 있도록 한다. 각 경매 중에 사용자는 해당 경매를 위해 만들어진 대화방에 참여할 수 있다. 경매가 완료되면 증서 토큰 소유권이 경매 낙찰자에 이전된다. 

<p>기본 구성
<li>발신 EOA에 의해 발행되어 메시지 재사용을 방지하는데 사용되는 일련번호</li>
<li>경매 댑: 벡엔드 스마트 컨트랙트 </li>
<li>댑 거버넌스</li>
<li>경매 댑: 프런트엔드 사용자 인터페이스</li>
<li>스웜 (데이터 스토리지)</li>
</p> 

<img width="877" alt="스크린샷 2019-11-27 오후 4 56 59" src="https://user-images.githubusercontent.com/39859458/69704596-16b42680-1137-11ea-8fe6-a40f58fdd99d.png">

#### 1) ERC721 대체 불가능한 '증서' 토큰(non-fungible 'deed' tokens)을 구현하는 스마트 컨트랙트(DeedRepository)
#### 2) 증서를 팔기 위해 경매(AuctionRepository)를 구현하는 스마트 컨트랙트
#### 3) Vue/Vuetify 자바스크립트 프레임워크를 사용하는 웹 프런트 엔드
#### 4) 이더리움 체인에 연결하는 web3.js 라이브러리(메타마스크 또는 다른 클라이언트를 통해)
#### 5) 이미지 같은 자원을 저장하는 스윔 클라이언트
#### 6) 모든 참여자를 위해 경매별 대화방을 개설하기 위한 위스퍼 클라이언트

-----------------------------------------------------------------------------------------------------------------
## 2-1 경매 댑: 백엔드 스마트 컨트랙트
- 두개의 스마트 컨트랙트(AuctionRepository, DeedRepository)를 사용하고, 두 컨트랙트는 애플리케이션을 지원하기 위해 이더리움 블록체인에 배포되어 있어야 한다. 


## 2-2 경매 댑: 프런트엔드 사용자 인터페이스
- 경매 댑의 컨트랙트가 배포되면 사용자는 선호하는 자바스크립트 콘솔과 web3.js또는 다른 web3 라이브러리를 사용하여 댑의 컨트랙트와 상호작용할 수 있다.</br>
- 컨트랙트를 배포한 후 frontend/src/config.js에서 프런트엔드 설정을 편집하고 DeedRepository 및 AuctionRepository컨트랙트의 주소를 배포된 대로 입력하라. 프런트엔드 애플리케이션 또한 JSON-RPC및 WebSockets 인터페이스를 제공하는 이더리움 노드에 대한 접근이 필요하다. 프론트엔드를 구성했으면 로컬 시스템에서 웹서버를 사용하여 프런트엔드를 실행하라. 


<code>
$npm install</code></br>
<code>
$npm run dev
</code>


## 2-1. 경매 댑을 더 탈 중앙화하기
    - 모든 애플리케이션 코드를 스웜 또는 IPFS에 저장한다.
    - 이더리움 네임 서비스를 사용하여 네임을 참조하여 댑에 접근한다. 


## 2-2. 스웜에 경매 댑 저장하기 

#### 스윔 준비하기

      
#### 스윔에 파일 올리기 



-----------------------------------------------------------------------------------------------------------------


## 3. 이더리움 네임 서비스(ENS)
### 1) 이더리움 네임 서비스의 역사
### 2) ENS사양
### 3) 맨 아래 계층: 이름 소유자 및 리졸버
        - 네임해시 알고리즘
        - 유효한 이름을 선택하는 방법
        - 루트 노드 소유권
        - 리졸버
### 4) 중간 계층: .eth 노드
        - 비크레이 경매 
### 5) 최상위 계층: 증서
### 6) 이름 등록하기 
### 7) ENS이름 관리
        - ENS 하위 도메인 만들기
### 8) ENS 리졸버 
### 9) 스웜 해시로 이름 해석(콘텐츠)


-----------------------------------------------------------------------------------------------------------------

## 4. 앱에서부터 댑까지
 ERC721 증서를 위한 경매를 진행하기 위해 한쌍의 스마트 컨트랙트를 시작했다. 
이런 컨트랙트에는 통제권이나 특권을 가진 계정이 없도록 설계되어서 제대로 탈중앙화되어 운영된다. 우리는 댑이 편리하고 사용자 친화적인 인터페이스를 갖기 위해 자바스크립트로 구현된 프런트엔트를 추가하였다. 
경매댑은 탈중앙화 스토리지 시스템 스웜을 사용하여 이미지 같은 애플리케이션 자원을 저장한다. 
위스퍼를 사용하여 중ㅇ앙서버없이 각 경매마다 암호화된 대화방을 제공한다. </br>
 전체 프런트엔드를 스웜에 업로드했으므로 댑은 파일을 제공하기 위해 웹 서버에 의존하지 않는다. ENS를 사용하여 댑의 이름을 할당하고 프런트엔드의 스웜해시에 연결하여, 단순하며 기억하기 쉽게 사람이 읽을 수 있는 이름으로 사용자가 접근할 수 있도록 한다. 
 <img width="945" alt="스크린샷 2019-11-27 오후 5 20 34" src="https://user-images.githubusercontent.com/39859458/69706074-47e22600-113a-11ea-823b-c9fcabc71c22.png">



-----------------------------------------------------------------------------------------------------------------


# 목차 
- 댑이란 무엇인가?
    - 백엔드(스마트 컨트랙트)
    - 프론트엔드(웹 유저 인터페이스)
    - 데이터 스토리지
    - 탈중앙화 메시지 통신 프로토콜
- 기본 댑 사례: 경매 댑
    - 경매 댑: 벡엔드 스마트 컨트랙트
    - 경매 댑: 프런트엔드 사용자 인터페이스
- 경매 댑을 더 탈중앙화하기
- 스웜에 경매 댑 저장하기
    - 스웜 준비하기
    - 스웜에 파일올리기
- 이더리움 네임 서비스(ENS)
    - 이더리움 네임 서비스 역사
    - ENS 사양
    - 맨 아래 계층: 이름 소유자 및 리졸버
    - 중간 계층: .eth 노드
    - 최상위 계층: 증서
    - 이름 등록하기
    - ENS 이름 관리
    - ENS 리졸버
    - 스웜 해시로 이름 해석(콘텐츠)
- 앱에서부터 댑까지






