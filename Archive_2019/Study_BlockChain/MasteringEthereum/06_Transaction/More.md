## 트랜잭션 
- 일반적으로는 시스템 안에서 더 나눌 수 없는 처리 단위.
- 블록체인에서는 토큰 소유권을 포함하는 데이터를 주고 받는 것을 뜻한다. 
- 작성자의 전자 서명을 적용해 코인 및 토큰 발행을 증명하거나..(무결성)

## 주소(Address)
- 공개 키 암호로 암호화폐를 받거나 보내는 단위로 다루는 임의 문자열 
- 공개 키를 바탕으로 만들고 비밀 키가 있는 프로그램으로 암호화폐의 이용 권한을 얻을 수 있다. 

## 블록(Block)
- 여러 거래를 모아 만든 데이터의 단위
- 거래를 블록에 저장하면 올바른 거래인지 검증하며, 작업 증명 알고리즘등을 이용해 이중 지급을 막는다. 
- 블록의 이름: TXID라 불리는 블록의 해시값이다. 이 블록의 해시값은 블록의 헤더 정보를 모두 합산한 후 SHA256으로 변환된 값이다. 
- 블록에는 블록의 이름이 있고 그 이름은 Height(높이)로 표
- 블록의 구성: Hash, previousHash, Header, Body(거래 내역들 : 그래서 body란 용어 대신 transaction이라고 표현하기도 함)

<img width="631" alt="structure1" src="https://user-images.githubusercontent.com/39859458/68288468-d2011680-00c7-11ea-9f66-9df078fa3c16.png">
<img width="631" alt="structure2" src="https://user-images.githubusercontent.com/39859458/68288519-e9400400-00c7-11ea-8629-4013617ed098.png">


## 블록높이(Block Height)
새로운 블록을 생성할 때는 먼저 생성한 블록의 해시값을 저장해야한다. 
- 블록 높이는 해시값을 포함해 연결된 블록의 전체 개수를 뜻한다. 
- 블록 높이가 0이면 맨처음 생성한 블록이며 이를 **제네시스블록(genesis block)**이라고 한다. 
- 거래와 블록안의 타임스탬프는 블록을 만든 사람이 자유롭게 선정 가능하다. **하지만** 타임스탬프 기록으로 결정한 블록 생성 순서는 신뢰도를 보장한다. 
<img width="631" alt="height1" src="https://user-images.githubusercontent.com/39859458/68288778-60759800-00c8-11ea-8556-677fd3504b37.png">
<img width="631" alt="height2" src="https://user-images.githubusercontent.com/39859458/68288813-73886800-00c8-11ea-8e96-0eae46542ab2.png">

## 이더리움 네트워크의 종류
- 메인넷: 여러 사람이 실제로 이더리움을 사용하는 네트워크. ('이더' 를 얻으려면 채굴하거나 거래소 등에서 사야 합니다.)
- 테스트넷: 임시 네트워크로 롭튼(Ropsten), 코밴(Kovan), 린키비(Rinkeby)라는 세 가지 테스트넷이 유명.
        - 롭튼: 메인넷과 같은 작업 증명 알고리즘 기반의 애플리케이션을 실행할 수 있는 테스트넷
               블록을 생성하려면 채굴해야 한다는 점까지 같다. DApp테스트용으로 좋다. 
        - 코밴: 권한 증명 알고리즘 기반의 애플리케이션을 실행할 수 있다. 블록 간격이 짧아 개발과 테스트가 쉽다. 
        - 린키비: (이더리움재단에서 만듬) 이더리움 개선 제안(EIPs)의 225번 논의에서 만들어졌다. 코밴 테스트넷에 블록 생성 제한이 있고, 다른 이더리움 클라이언트와 호환성이 약하다는 이유로 만듬.  
- 사설망: 
    - 네트워크에서 말하는 사설망과 뜻이 같다. 
    - 즉, 필요에 따라 개발자가 만드는 네트워크. 이더를 얻으려면 채굴해야 하지만 채굴 난이도가 낮다. 

<img width="631" alt="network" src="https://user-images.githubusercontent.com/39859458/68388704-9ab46780-01a4-11ea-8846-d74c6cfab89b.png">

## P2P Network
<img width="631" alt="P2P" src="https://user-images.githubusercontent.com/39859458/68288351-949c8900-00c7-11ea-9617-81639f7f67a4.png">

## 가스
- 가스는 이더리움에서 애플리케이션을 실행할 때 지급하는 네트워크 수수료 이다. 
- 가스는 악성프로그램에 많은 수수료를 부과해서 자율적으로 문제를 해결한다. 

## 개발환경 구축하기. 
(본인 pc에)
### 1. Go Ethereum의 클라이언트인 Geth설치
(사설망을 이용한다.) 
### 3. 0번째 블록생성해 보기 (제네시스 블록 생성해 보기)
### 3. 외부 계정 주소 만들기
    - personal.newAccount("<비밀번호")
    - eth.accounts
### 4. 블록내용 확인 
    - eth.getBlock(0)
### 5. 채굴
    - miner.start(<스레드 수>)
(채굴에 성공했다 가정하면,)
### 6. 잔액확인 (보상)
    - eth.getBalance(eth.account[0])
### 7. 송금
    - eth.sendTransaction({from:, to:, value: })
##### 송금액은 wei단위로 지정한다.!!!
    - web3.fromWei
    - web3.toWei
##### 예제: 계좌0번에서 계좌2번에 5이더 송금
    - 1) 잔액확인
    - web3.fromWei(eth.getBalance(eth.accounts[2]))
    - 2) 송금
    - eth.sendTransaction({from: eth.accounts[0], to: eth.accounts[2], value: web3.toWei(5, "ether")})
    - >"0xbf3...." 16진수 거래 해시값을 출력.
    - 3) 거래확인
    - eth.getTransaction("0xbf3....")
    - 4) 영수증 확인
    - eth.getTransactionReceipt("0xbf3....)

#### 8. 거래정보
거래정보는 트리구조로 저장된다. 


## genesisblock.json파일
<img width="631" alt="P2P" src="https://user-images.githubusercontent.com/39859458/68292452-3b385800-00cf-11ea-88aa-121ba311e6d0.png">


## BlockHeader.json파일
<img width="631" alt="bh" src="https://user-images.githubusercontent.com/39859458/68389069-7016de80-01a5-11ea-9006-7ef042a0885d.png">
<img width="631" alt="bh" src="https://user-images.githubusercontent.com/39859458/68389087-7d33cd80-01a5-11ea-82ac-c42d518efd54.png">
