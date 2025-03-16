import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { Box, Button, Typography } from "@mui/material";
import NavigateNextIcon from "@mui/icons-material/NavigateNext";
import background from "../../assets/background.png";
import { useState } from "react";
import dayjs, { Dayjs } from "dayjs";
const Birthday = () => {
  const [date, setDate] = useState<Dayjs | null>(dayjs());

  const handleBirthdaySelection = (userBirthday: Dayjs) => {
    setDate(userBirthday);
    const currentDate = dayjs();
    const age = userBirthday.diff(currentDate, "year");
    console.log(age);
    
  };

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
        paddingTop={"25vh"}
        gap={10}
        sx={{
          color: "#e5446d",
        }}
      >
        <Typography
          variant="h1"
          sx={{
            fontFamily: "'Bebas Neue', Roboto",
            fontSize: "50px",
          }}
        >
          What is your birthday?
        </Typography>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DatePicker
            value={date}
            onChange={(value: Dayjs | null) =>
              handleBirthdaySelection(value as Dayjs)
            }
          />
        </LocalizationProvider>
      </Box>

      <Button
        style={{
          backgroundColor: "#e5446d",
          marginTop: "10%",
          marginLeft: "80%",
          borderRadius: "200px",
          minWidth: "200px",
          minHeight: "200px",
        }}
      >
        <NavigateNextIcon style={{ color: "#edf6f9", fontSize: "100px" }} />
      </Button>
    </div>
  );
};
export default Birthday;
