/**경매에 사용하기위한 ERC721 증서 토큰

pragma solidity ^0.4.17;
import "./ERC721/ERC721Token.sol";

/**
 * @title ERC721 증서 저장소
 * 이 컨트랙트는 사용자가 등록한 증서의 목록을 포함한다.
 * 이것은 토큰(증서)를 작성하여 저장소에 추가하는 방법을 보여주는 데모다.
 */
contract DeedRepository is ERC721Token {
  /**
  * @dev name과 symbol이 있는 DeedRepository를 생성한다.
  * @param _name은 저장소의 이름을 나타내는 문자열이다.
  * @param _symbol은 저장소의 상징을 나타내는 문자열이다.
  */
  function DeedRepository(string _name, string _symbol)
      public ERC721Token(_name, _symbol) {}
  
  /**
  * @dev 새로운 증서을 등록하기 위한 public함수
  * @dev ERC721Token minter를 호출한다.
  * @param _tokenId는 구체적인 증서를 나타내기 위한 부호 없는 정수(uint256)이다.
  * @param _uri는 메타데이터 /uri를 포함하는 문자열이다.
  */
  function registerDeed(unit256 _tokenId, string _uri) public {
      _mint(msg.sendoer, tokenId);
      addDeedMetadata(_tokenId, _uri);
      emit DeedRegistered(msg.sender, _tokenId);
  }
  
  /**
  * @dev 증서에 메타데이터를 추가하는 방법
  * @param _tokenId는 구체적인 증서를 나타낸다.
  * @param _uri는 주어진 증서의 특징을 설명하는 텍스트
  * @return 저장송에 증서 메타데이터가 추가되었는지 여부를 반환한다.
  */
  function addDeedMetadata(uint256 _tokenId, string _uri) public returns(bool){
      _setTokenURI(_tokenId, _uri);
      return true;
  }
  
  /**
  * @dev 증서/토큰이 등록되면 이벤트가 트리거된다.
  * @param _by 등록지의 주소다
  * @param _tokenId는 특정 증서를 나타내기 위한 부호 없는 정수(unit256)이다.
  */
  event DeedRegistered(address _by, unit256 _tokenId);
}
