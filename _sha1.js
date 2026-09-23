function sha1(str){
  function rotl(n,s){return ((n<<s)|(n>>>(32-s)))>>>0;}
  var utf8=unescape(encodeURIComponent(str)), bytes=[];
  for(var i=0;i<utf8.length;i++)bytes.push(utf8.charCodeAt(i));
  var ml=bytes.length*8;
  bytes.push(0x80);
  while(bytes.length%64!==56)bytes.push(0);
  for(var i=7;i>=0;i--)bytes.push(Math.floor(ml/Math.pow(2,i*8))&0xff);
  var h0=0x67452301,h1=0xEFCDAB89,h2=0x98BADCFE,h3=0x10325476,h4=0xC3D2E1F0;
  for(var i=0;i<bytes.length;i+=64){
    var w=new Array(80),j;
    for(j=0;j<16;j++)w[j]=((bytes[i+j*4]<<24)|(bytes[i+j*4+1]<<16)|(bytes[i+j*4+2]<<8)|bytes[i+j*4+3])>>>0;
    for(j=16;j<80;j++)w[j]=rotl(w[j-3]^w[j-8]^w[j-14]^w[j-16],1);
    var a=h0,b=h1,c=h2,d=h3,e=h4,f,k,t;
    for(j=0;j<80;j++){
      if(j<20){f=(b&c)|((~b)&d);k=0x5A827999;}
      else if(j<40){f=b^c^d;k=0x6ED9EBA1;}
      else if(j<60){f=(b&c)|(b&d)|(c&d);k=0x8F1BBCDC;}
      else{f=b^c^d;k=0xCA62C1D6;}
      t=(rotl(a,5)+(f>>>0)+e+k+w[j])>>>0;
      e=d;d=c;c=rotl(b,30);b=a;a=t;
    }
    h0=(h0+a)>>>0;h1=(h1+b)>>>0;h2=(h2+c)>>>0;h3=(h3+d)>>>0;h4=(h4+e)>>>0;
  }
  return [h0,h1,h2,h3,h4].map(function(x){return ('00000000'+x.toString(16)).slice(-8);}).join('');
}
