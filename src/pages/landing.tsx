import { Box, Button, Typography } from "@mui/material";
import background from "../../assets/background.png";

const Landing = () => {
  return (
    <div
      style={{
        backgroundImage: `url(${background})`,
        backgroundPosition: "center -300px",
        backgroundSize: "cover",
        backgroundRepeat: "no-repeat",
        width: "100vw",
        height: "100vh",
      }}
    >
      <Typography
        variant="h1"
        style={{
          color: "#0b1d51",
          textAlign: "center",
          paddingTop: "30vh",
          fontFamily: "'Bebas Neue', Roboto",
          fontSize: "130px",}}
      >
        FIND YOUR MATCH
      </Typography>

      <Box
        display={"flex"}
        justifyContent={"center"}
        alignItems={"center"}
        flexDirection={"column"}
        paddingTop={"10vh"}
        gap={8}
      >
        <Button
          variant="contained"
          size="large"
          style={{
            backgroundColor: "#edf6f9",
            color: "#0b1d51",
            minWidth: "300px",
            borderRadius: "50px",
            minHeight: "70px",
            fontFamily: "'Bebas Neue', Roboto",
            fontSize: "40px"
            
          }}
        >
          Login
        </Button>

        <Button
          variant="contained"
          size="large"
          style={{
            backgroundColor: "#edf6f9",
            color: "#0b1d51",
            minWidth: "300px",
            borderRadius: "50px",
            minHeight: "70px",
            fontFamily: "'Bebas Neue', Roboto",
            fontSize: "40px"
          }}
        >
          Sign up
        </Button>
      </Box>
    </div>
  );
};

export default Landing;
