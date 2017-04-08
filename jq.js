<head>
<script src="jquery-3.2.0.min"></script>
</head>
// dont forget to include jQuery code
// preferably with .noConflict() in order not to break the site scripts
if (window.location.indexOf("https://academia.srmuniv.ac.in/") > -1) {
    // Lets login to Gmail
    jQuery("#username").val("saksham_singhal@srmuniv.edu.in");
    jQuery("#password").val("****!@#****");
    jQuery("#gaia_loginform").submit();
}