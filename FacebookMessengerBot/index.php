<?php

$challenge = $_REQUEST['hub_challenge'];
$verify_token = $_REQUEST['hub_verify_token'];

if ($verify_token === 'make_me_an_offer_i_can_not_refuse') {
echo $challenge;
}
else
{
echo "Failed validation. Make sure the validation tokens match.";
   
}
?>