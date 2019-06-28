<?php
	$servername="localhost";
	$username="root";
	$password="root";
	$db = "aawaz";
	$conn =mysqli_connect($servername,$username,$password,$db);
		
	if(!$conn)
	{	
		echo "Error in connection db".$conn.error();
	}

	$weekday_sql = "select count(date_time) from analytics_app_open where date_time >= (CURDATE()-INTERVAL DAYOFWEEK(CURDATE()-2) DAY);";
	$result = mysqli_query($conn, $weekday_sql);
	
	if (mysqli_num_rows($result) > 0)
	{
		// output data of each row
		while($row = mysqli_fetch_assoc($result))
		{
			$targetValue = $row["count(date_time)"];
		}
	} 
	else 
	{
		echo "0 results";
	}
	mysqli_close($conn);
	?>

<!doctype html>
<html lang="en">

<head>
	<title>Dashboard</title>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
	<!-- VENDOR CSS -->
	<link rel="stylesheet" href="assets/vendor/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" href="assets/vendor/font-awesome/css/font-awesome.min.css">
	<link rel="stylesheet" href="assets/vendor/linearicons/style.css">
	<link rel="stylesheet" href="assets/vendor/chartist/css/chartist-custom.css">
	<!-- MAIN CSS -->
	<link rel="stylesheet" href="assets/css/main.css">
	<!-- GOOGLE FONTS -->
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700" rel="stylesheet">
</head>

<body>
	<!-- WRAPPER -->
	<div id="wrapper">
		<!-- LEFT SIDEBAR -->
		<div id="sidebar-nav" class="sidebar">
			<div class="sidebar-scroll">
				<nav>
					<ul class="nav">
						<li><a href="today.php" class=""><i class=""></i> <span>Today's data</span></a></li>
						<li><a href="this_week.php" class=""><i class=""></i> <span>This week data</span></a></li>
						<li><a href="7_days.php" class=""><i class=""></i> <span>Last 7 days data</span></a></li>
						<li><a href="15_days.php" class=""><i class=""></i> <span>Last 15 days data</span></a></li>
						<li><a href="1_month.php" class=""><i class=""></i> <span>Last 1 month data</span></a></li>
						<li><a href="3_months.php" class=""><i class=""></i> <span>Last 3 month data</span></a></li>
						<li><a href="weekdays.php" class="active"><i class=""></i> <span>Weekdays data</span></a></li>
						<li><a href="weekend.php" class=""><i class=""></i> <span>Weekends data</span></a></li>
					</ul>
				</nav>
			</div>
		</div>
		<!-- END LEFT SIDEBAR -->
		<!-- MAIN -->
		<div class="main">
			<!-- MAIN CONTENT -->
			<div class="main-content">
				<div class="container-fluid">
					<h2 class="page_title">Logs</h2>
					<!-- OVERVIEW -->
					<div class="panel panel-headline">
						<div class="panel-heading">
							<h3 class="panel-title">Weekdays Overview</h3>
						</div>
						<div class="panel-body">
							<div class="row">
								<div class="col-md-3">
									<div class="metric">
										<p>
											<span class="number"><?php echo $targetValue; ?></span>
											<span class="title">Logs</span>
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- END OVERVIEW -->
				</div>
			</div>
			<!-- END MAIN CONTENT -->
		</div>
		<!-- END MAIN -->
	</div>
	<!-- END WRAPPER -->
</body>

</html>
