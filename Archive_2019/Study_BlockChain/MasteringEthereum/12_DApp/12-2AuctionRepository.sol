//** 주요 경매 댑 스마트 컨트랙트

contract AuctionRepository {

    // 모든 actions의 배열
    Auction[] public auctions;
    
    // action 인덱스에서 사용자 bid로 매핑
    mapping(uint256 => Bid[]) public auctionBifs;
    
    // owner에서 auction으로 매핑
    mapping(address => unit[]) public actionOwner;
    
    // 입찰자와 amount를 포함한 Bid 구조체
    struct Bid {
        address from;
        uint256 amount;
    }
    
    // 필요한 정보를 모두 담고 있는 Auction 구조체
    struct Auction {
        string name;
        uint256 blockDeadline;
        uint256 startPrice;
        string metadata;
        uint256 deedId;
        address deedRepositoryAddress;
        address owner;
        bool active;
        bool finalized;
    }
    
//** AuctionRepository컨트랙트는 다음 기능을 사용하여 모든 경매를 관리한다.
getCount()
getBidsCount(unit _actionId)
getAuctionsOf(address _owner)
getCurrentBid(uint _auctionId)
getAuctionsCountOfOwner(address _owner)
getAuctionById(uint _actionId)
createAuction(address _deedRepositoryAddress, unit256 _deedId,
              string _auctionTitle, string_metadata, uint256 _startPrice,
              unit _blockDeadline)
approveAndTransfer(address _from, address _to, address _deedRepositoryAddress, unit256 _deedId)
cancleAuction(unit _auctionId)
finalizeAuction(unit _auctionId)
bidOnauction(unit _auctionId)

//* truffle을 사용하여 (롭스텐)이더리움 블록체인에 컨트랙트를 배포할 수 있다.
$ cd code/auction_dapp/backend
$ truffle init
$ truffle compile
$ truffle migrate --network ropsten
