import { Box, Typography } from "@mui/material";
import background from "../../assets/background.png";
const Name = () => {
  return (
    <div
      style={{
        backgroundImage: `url(${background})`,
        backgroundPosition: "center -300px",
        backgroundSize: "cover",
        backgroundRepeat: "no-repeat",
        minHeight: "100vh",
        minWidth: "100vw",
        position: "absolute",
        top: "0",
        left: "0",
        right: "0",
        bottom: "0",
      }}
    >
      <Box
        display={"flex"}
        justifyContent={"center"}
        alignItems={"center"}
        flexDirection={"column"}
        paddingTop={"10vh"}
        gap={8}
      >
        <Typography>What is your name?</Typography>
      </Box>
    </div>
  );
};

export default Name;
