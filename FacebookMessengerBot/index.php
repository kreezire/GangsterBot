<?php
if (isset($_POST)) {
    // do post
}
else if(isset($_GET)) {
    // do get
	$json = json_encode($_GET);
	$challenge = $json['hub_challenge'];
	$verify_token = $json['hub_verify_token'];

	if ($verify_token === 'make_me_an_offer_i_can_not_refuse') {
		echo $challenge;
	}
	else
	{
	echo "Failed validation. Make sure the validation tokens match.";
   
	}
}
else{
	echo "Invalid Request.";
}

?>