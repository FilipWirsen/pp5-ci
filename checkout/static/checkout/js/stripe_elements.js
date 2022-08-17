/*
    Core logic/payment flow for this comes from below
    (and the Boutique Ado project by Code Institute)
    https://stripe.com/docs/payments/accept-a-payment
    
    CSS from here (but customized): 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
var client_secret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Anaheim", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');